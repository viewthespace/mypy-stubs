from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.models.dag import DAG as DAG
from airflow.models.dagcode import DagCode as DagCode
from airflow.serialization.serialized_objects import SerializedDAG as SerializedDAG
from airflow.settings import json as json
from airflow.utils import db as db, timezone as timezone
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from sqlalchemy.orm import Session as Session
from typing import Any, Optional

log: Any

class SerializedDagModel(Base):
    __tablename__: str
    dag_id: Any
    fileloc: Any
    fileloc_hash: Any
    data: Any
    last_updated: Any
    dag_hash: Any
    __table_args__: Any
    def __init__(self, dag) -> None: ...
    @classmethod
    def write_dag(cls, dag: DAG, min_update_interval: Optional[int] = ..., session: Any | None = ...): ...
    @classmethod
    def read_all_dags(cls, session: Any | None = ...): ...
    @property
    def dag(self): ...
    @classmethod
    def remove_dag(cls, dag_id, session: Any | None = ...) -> None: ...
    @classmethod
    def remove_deleted_dags(cls, alive_dag_filelocs, session: Any | None = ...) -> None: ...
    @classmethod
    def has_dag(cls, dag_id, session: Any | None = ...): ...
    @classmethod
    def get(cls, dag_id, session: Any | None = ...): ...
    @classmethod
    def get_last_updated_datetime(cls, dag_id, session): ...
