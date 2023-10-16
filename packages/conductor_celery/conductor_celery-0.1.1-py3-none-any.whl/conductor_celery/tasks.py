import logging
from dataclasses import asdict, dataclass

from celery import Task, shared_task

from conductor_celery.utils import configure_runner
from conductor_celery.utils import update_task as real_update_task

logger = logging.getLogger(__name__)


class ConductorPollTask(Task):
    pass


@dataclass
class PooledConductorTask:
    task_id: str
    workflow_instance_id: str
    worker_id: str
    input_data: dict


class ConductorTask(Task):
    """
    This handle a canductor task
    """

    def __call__(self, *args, **kwargs):
        server_api_url = self.app.conf["conductor_server_api_url"]
        logger.debug(f"ConductorTask configure_runner: {server_api_url}")

        runner = configure_runner(server_api_url=server_api_url, name=self.name, debug=True)

        if self.request.retries == 0:
            conductor_task = runner.poll_task()

            if conductor_task.task_id is None:
                return

            pct = PooledConductorTask(
                input_data=conductor_task.input_data,
                task_id=conductor_task.task_id,
                workflow_instance_id=conductor_task.workflow_instance_id,
                worker_id=conductor_task.worker_id,
            )

            kwargs = conductor_task.input_data
            self.request.kwargs = conductor_task.input_data
            self.request.args = ()
            if not self.request.headers:
                self.request.headers = {"conductor": asdict(pct)}
            else:
                self.request.headers["conductor"] = asdict(pct)
        else:
            conductor_task = PooledConductorTask(**self.request.headers["conductor"])

        logger.info(f"running task:{conductor_task.task_id} workflow: {conductor_task.workflow_instance_id}")

        try:
            ret = self.run(**kwargs)
            status = "COMPLETED"
        except Exception as exc:
            logger.exception(
                f"Error running task:{conductor_task.task_id} workflow: {conductor_task.workflow_instance_id}"
            )
            ret = {"error": str(exc)}
            status = "FAILED"

            if self.request.retries == self.max_retries:
                runner.update_task(
                    real_update_task(
                        conductor_task.task_id,
                        conductor_task.workflow_instance_id,
                        conductor_task.worker_id,
                        ret,
                        status,
                    )
                )
            raise

        runner.update_task(
            real_update_task(
                conductor_task.task_id, conductor_task.workflow_instance_id, conductor_task.worker_id, ret, status
            )
        )
        return ret


@shared_task(bind=True)
def update_task(self, name, task_id, workflow_instance_id, worker_id, values):
    runner = configure_runner(server_api_url=self.app.conf["conductor_server_api_url"], name=name, debug=True)
    runner.update_task(real_update_task(task_id, workflow_instance_id, worker_id, values, "COMPLETED"))
