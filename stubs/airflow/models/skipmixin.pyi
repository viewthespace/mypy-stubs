from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils import timezone as timezone
from airflow.utils.db import create_session as create_session, provide_session as provide_session
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.state import State as State
from typing import Any

XCOM_SKIPMIXIN_KEY: str
XCOM_SKIPMIXIN_SKIPPED: str
XCOM_SKIPMIXIN_FOLLOWED: str

class SkipMixin(LoggingMixin):
    def skip(self, dag_run, execution_date, tasks, session: Any | None = ...) -> None: ...
    def skip_all_except(self, ti, branch_task_ids) -> None: ...
