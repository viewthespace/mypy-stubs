from airflow.configuration import conf as conf
from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.serialization.helpers import serialize_template_field as serialize_template_field
from airflow.settings import json as json
from airflow.utils.db import provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class RenderedTaskInstanceFields(Base):
    __tablename__: str
    dag_id: Any
    task_id: Any
    execution_date: Any
    rendered_fields: Any
    task: Any
    ti: Any
    def __init__(self, ti, render_templates: bool = ...) -> None: ...
    @classmethod
    def get_templated_fields(cls, ti, session: Any | None = ...): ...
    def write(self, session: Any | None = ...) -> None: ...
    @classmethod
    def delete_old_records(cls, task_id, dag_id, num_to_keep=..., session: Any | None = ...) -> None: ...
