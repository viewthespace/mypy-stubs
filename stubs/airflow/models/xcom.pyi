from airflow.configuration import conf as conf
from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.utils import timezone as timezone
from airflow.utils.db import provide_session as provide_session
from airflow.utils.helpers import as_tuple as as_tuple
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

log: Any
MAX_XCOM_SIZE: int
XCOM_RETURN_KEY: str

class BaseXCom(Base, LoggingMixin):
    __tablename__: str
    id: Any
    key: Any
    value: Any
    timestamp: Any
    execution_date: Any
    task_id: Any
    dag_id: Any
    __table_args__: Any
    def init_on_load(self) -> None: ...
    @classmethod
    def set(cls, key, value, execution_date, task_id, dag_id, session: Any | None = ...) -> None: ...
    @classmethod
    def get_one(cls, execution_date, key: Any | None = ..., task_id: Any | None = ..., dag_id: Any | None = ..., include_prior_dates: bool = ..., session: Any | None = ...): ...
    @classmethod
    def get_many(cls, execution_date, key: Any | None = ..., task_ids: Any | None = ..., dag_ids: Any | None = ..., include_prior_dates: bool = ..., limit: int = ..., session: Any | None = ...): ...
    @classmethod
    def delete(cls, xcoms, session: Any | None = ...) -> None: ...
    @staticmethod
    def serialize_value(value): ...

def resolve_xcom_backend(): ...

XCom: Any
