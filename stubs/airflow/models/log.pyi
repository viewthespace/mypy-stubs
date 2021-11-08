from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.utils import timezone as timezone
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class Log(Base):
    __tablename__: str
    id: Any
    dttm: Any
    dag_id: Any
    task_id: Any
    event: Any
    execution_date: Any
    owner: Any
    extra: Any
    __table_args__: Any
    def __init__(self, event, task_instance, owner: Any | None = ..., extra: Any | None = ..., **kwargs) -> None: ...
