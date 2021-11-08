from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class TaskFail(Base):
    __tablename__: str
    id: Any
    task_id: Any
    dag_id: Any
    execution_date: Any
    start_date: Any
    end_date: Any
    duration: Any
    __table_args__: Any
    def __init__(self, task, execution_date, start_date, end_date) -> None: ...
