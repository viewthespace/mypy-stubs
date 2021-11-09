from airflow.models.base import Base as Base
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class ImportError(Base):
    __tablename__: str
    id: Any
    timestamp: Any
    filename: Any
    stacktrace: Any
