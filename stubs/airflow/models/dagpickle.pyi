from airflow.models.base import Base as Base
from airflow.utils import timezone as timezone
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class DagPickle(Base):
    id: Any
    pickle: Any
    created_dttm: Any
    pickle_hash: Any
    __tablename__: str
    dag_id: Any
    def __init__(self, dag) -> None: ...
