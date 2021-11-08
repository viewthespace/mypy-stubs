from airflow import executors as executors, models as models
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.settings import Stats as Stats
from airflow.utils import helpers as helpers, timezone as timezone
from airflow.utils.db import create_session as create_session, provide_session as provide_session
from airflow.utils.helpers import convert_camel_to_snake as convert_camel_to_snake
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from airflow.utils.state import State as State
from typing import Any

class BaseJob(Base, LoggingMixin):
    __tablename__: str
    id: Any
    dag_id: Any
    state: Any
    job_type: Any
    start_date: Any
    end_date: Any
    latest_heartbeat: Any
    executor_class: Any
    hostname: Any
    unixname: Any
    __mapper_args__: Any
    __table_args__: Any
    heartrate: Any
    executor: Any
    max_tis_per_query: Any
    def __init__(self, executor: Any | None = ..., heartrate: Any | None = ..., *args, **kwargs) -> None: ...
    @classmethod
    def most_recent_job(cls, session: Any | None = ...): ...
    def is_alive(self, grace_multiplier: float = ...): ...
    def kill(self, session: Any | None = ...) -> None: ...
    def on_kill(self) -> None: ...
    def heartbeat_callback(self, session: Any | None = ...) -> None: ...
    def heartbeat(self) -> None: ...
    def run(self) -> None: ...
    def reset_state_for_orphaned_tasks(self, filter_by_dag_run: Any | None = ..., session: Any | None = ...): ...
