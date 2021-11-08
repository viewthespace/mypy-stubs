from airflow import settings as settings
from airflow.configuration import conf as conf
from airflow.dag.base_dag import BaseDagBag as BaseDagBag
from airflow.exceptions import AirflowClusterPolicyViolation as AirflowClusterPolicyViolation, AirflowDagCycleException as AirflowDagCycleException
from airflow.executors import get_default_executor as get_default_executor
from airflow.settings import Stats as Stats
from airflow.utils import timezone as timezone
from airflow.utils.dag_processing import correct_maybe_zipped as correct_maybe_zipped, list_py_file_paths as list_py_file_paths
from airflow.utils.db import provide_session as provide_session
from airflow.utils.helpers import pprinttable as pprinttable
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.timeout import timeout as timeout
from typing import Any

class DagBag(BaseDagBag, LoggingMixin):
    CYCLE_NEW: int
    CYCLE_IN_PROGRESS: int
    CYCLE_DONE: int
    DAGBAG_IMPORT_TIMEOUT: Any
    UNIT_TEST_MODE: Any
    SCHEDULER_ZOMBIE_TASK_THRESHOLD: Any
    dag_folder: Any
    dags: Any
    file_last_changed: Any
    executor: Any
    import_errors: Any
    has_logged: bool
    store_serialized_dags: Any
    dags_last_fetched: Any
    def __init__(self, dag_folder: Any | None = ..., executor: Any | None = ..., include_examples=..., safe_mode=..., store_serialized_dags: bool = ...) -> None: ...
    def size(self): ...
    @property
    def dag_ids(self): ...
    def get_dag(self, dag_id): ...
    def process_file(self, filepath, only_if_updated: bool = ..., safe_mode: bool = ...): ...
    def kill_zombies(self, zombies, session: Any | None = ...) -> None: ...
    def bag_dag(self, dag, parent_dag, root_dag) -> None: ...
    dagbag_stats: Any
    def collect_dags(self, dag_folder: Any | None = ..., only_if_updated: bool = ..., include_examples=..., safe_mode=...): ...
    def collect_dags_from_db(self) -> None: ...
    def dagbag_report(self): ...
