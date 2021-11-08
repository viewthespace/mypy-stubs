from airflow.models.base import Base as Base
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class KnownEventType(Base):
    __tablename__: str
    id: Any
    know_event_type: Any

class KnownEvent(Base):
    __tablename__: str
    id: Any
    label: Any
    start_date: Any
    end_date: Any
    user_id: Any
    known_event_type_id: Any
    reported_by: Any
    event_type: Any
    description: Any
