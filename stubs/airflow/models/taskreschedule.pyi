from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.utils.db import provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class TaskReschedule(Base):
    __tablename__: str
    id: Any
    task_id: Any
    dag_id: Any
    execution_date: Any
    try_number: Any
    start_date: Any
    end_date: Any
    duration: Any
    reschedule_date: Any
    __table_args__: Any
    def __init__(self, task, execution_date, try_number, start_date, end_date, reschedule_date) -> None: ...
    @staticmethod
    def find_for_task_instance(task_instance, session): ...
