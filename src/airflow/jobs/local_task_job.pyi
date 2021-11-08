from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.jobs.base_job import BaseJob as BaseJob
from airflow.settings import Stats as Stats
from airflow.task.task_runner import get_task_runner as get_task_runner
from airflow.utils import timezone as timezone
from airflow.utils.db import provide_session as provide_session
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.state import State as State
from typing import Any

class LocalTaskJob(BaseJob):
    __mapper_args__: Any
    task_instance: Any
    dag_id: Any
    ignore_all_deps: Any
    ignore_depends_on_past: Any
    ignore_task_deps: Any
    ignore_ti_state: Any
    pool: Any
    pickle_id: Any
    mark_success: Any
    terminating: bool
    def __init__(self, task_instance, ignore_all_deps: bool = ..., ignore_depends_on_past: bool = ..., ignore_task_deps: bool = ..., ignore_ti_state: bool = ..., mark_success: bool = ..., pickle_id: Any | None = ..., pool: Any | None = ..., *args, **kwargs) -> None: ...
    def on_kill(self) -> None: ...
    def heartbeat_callback(self, session: Any | None = ...) -> None: ...
