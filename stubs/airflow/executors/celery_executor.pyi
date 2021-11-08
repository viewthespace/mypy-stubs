from airflow.config_templates.default_celery import DEFAULT_CELERY_CONFIG as DEFAULT_CELERY_CONFIG
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.executors.base_executor import BaseExecutor as BaseExecutor
from airflow.utils.module_loading import import_string as import_string
from airflow.utils.timeout import timeout as timeout
from typing import Any

log: Any
CELERY_FETCH_ERR_MSG_HEADER: str
CELERY_SEND_ERR_MSG_HEADER: str
OPERATION_TIMEOUT: Any
celery_configuration: Any
celery_configuration = DEFAULT_CELERY_CONFIG
app: Any

def execute_command(command_to_exec) -> None: ...

class ExceptionWithTraceback:
    exception: Any
    traceback: Any
    def __init__(self, exception, exception_traceback) -> None: ...

def fetch_celery_task_state(celery_task): ...
def send_task_to_executor(task_tuple): ...

class CeleryExecutor(BaseExecutor):
    tasks: Any
    last_state: Any
    def __init__(self) -> None: ...
    def start(self) -> None: ...
    def trigger_tasks(self, open_slots): ...
    def sync(self) -> None: ...
    def end(self, synchronous: bool = ...) -> None: ...
