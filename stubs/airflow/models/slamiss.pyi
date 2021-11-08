from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class SlaMiss(Base):
    __tablename__: str
    task_id: Any
    dag_id: Any
    execution_date: Any
    email_sent: Any
    timestamp: Any
    description: Any
    notification_sent: Any
    __table_args__: Any
