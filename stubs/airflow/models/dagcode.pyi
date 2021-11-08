from airflow.exceptions import AirflowException as AirflowException, DagCodeNotFound as DagCodeNotFound
from airflow.models import Base as Base
from airflow.settings import STORE_DAG_CODE as STORE_DAG_CODE
from airflow.utils import timezone as timezone
from airflow.utils.db import provide_session as provide_session
from airflow.utils.file import correct_maybe_zipped as correct_maybe_zipped, open_maybe_zipped as open_maybe_zipped
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

log: Any

class DagCode(Base):
    __tablename__: str
    fileloc_hash: Any
    fileloc: Any
    last_updated: Any
    source_code: Any
    def __init__(self, full_filepath, source_code: Any | None = ...) -> None: ...
    def sync_to_db(self, session: Any | None = ...) -> None: ...
    @classmethod
    def bulk_sync_to_db(cls, filelocs, session: Any | None = ...) -> None: ...
    @classmethod
    def remove_deleted_code(cls, alive_dag_filelocs, session: Any | None = ...) -> None: ...
    @classmethod
    def has_dag(cls, fileloc, session: Any | None = ...): ...
    @classmethod
    def get_code_by_fileloc(cls, fileloc): ...
    @classmethod
    def code(cls, fileloc): ...
    @staticmethod
    def dag_fileloc_hash(full_filepath): ...
