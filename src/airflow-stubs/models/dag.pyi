import jinja2
from airflow import settings as settings, utils as utils
from airflow.configuration import conf as conf
from airflow.dag.base_dag import BaseDag as BaseDag
from airflow.exceptions import AirflowDagCycleException as AirflowDagCycleException, AirflowException as AirflowException, DagNotFound as DagNotFound, TaskNotFound as TaskNotFound
from airflow.executors import LocalExecutor as LocalExecutor, get_default_executor as get_default_executor
from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.dagcode import DagCode as DagCode
from airflow.models.dagpickle import DagPickle as DagPickle
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.taskinstance import TaskInstance as TaskInstance, clear_task_instances as clear_task_instances
from airflow.settings import MIN_SERIALIZED_DAG_UPDATE_INTERVAL as MIN_SERIALIZED_DAG_UPDATE_INTERVAL, STORE_SERIALIZED_DAGS as STORE_SERIALIZED_DAGS
from airflow.utils import timezone as timezone
from airflow.utils.dag_processing import correct_maybe_zipped as correct_maybe_zipped
from airflow.utils.dates import cron_presets as cron_presets
from airflow.utils.db import provide_session as provide_session
from airflow.utils.helpers import validate_key as validate_key
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.sqlalchemy import Interval as Interval, UtcDateTime as UtcDateTime
from airflow.utils.state import State as State
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from typing import Any, Callable, Dict, Iterable, List, Optional, Type, Union

log: Any
ScheduleInterval = Union[str, timedelta, relativedelta]

def get_last_dagrun(dag_id, session, include_externally_triggered: bool = ...): ...

class DAG(BaseDag, LoggingMixin):
    user_defined_macros: Any
    user_defined_filters: Any
    default_args: Any
    params: Any
    fileloc: Any
    task_dict: Any
    timezone: Any
    start_date: Any
    end_date: Any
    schedule_interval: Any
    template_searchpath: Any
    template_undefined: Any
    parent_dag: Any
    last_loaded: Any
    safe_dag_id: Any
    max_active_runs: Any
    dagrun_timeout: Any
    sla_miss_callback: Any
    orientation: Any
    catchup: Any
    is_subdag: bool
    partial: bool
    on_success_callback: Any
    on_failure_callback: Any
    doc_md: Any
    is_paused_upon_creation: Any
    jinja_environment_kwargs: Any
    tags: Any
    def __init__(self, dag_id: str, description: Optional[str] = ..., schedule_interval: Optional[ScheduleInterval] = ..., start_date: Optional[datetime] = ..., end_date: Optional[datetime] = ..., full_filepath: Optional[str] = ..., template_searchpath: Optional[Union[str, Iterable[str]]] = ..., template_undefined: Type[jinja2.Undefined] = ..., user_defined_macros: Optional[Dict] = ..., user_defined_filters: Optional[Dict] = ..., default_args: Optional[Dict] = ..., concurrency: int = ..., max_active_runs: int = ..., dagrun_timeout: Optional[timedelta] = ..., sla_miss_callback: Optional[Callable] = ..., default_view: Optional[str] = ..., orientation: str = ..., catchup: bool = ..., on_success_callback: Optional[Callable] = ..., on_failure_callback: Optional[Callable] = ..., doc_md: Optional[str] = ..., params: Optional[Dict] = ..., access_control: Optional[Dict] = ..., is_paused_upon_creation: Optional[bool] = ..., jinja_environment_kwargs: Optional[Dict] = ..., tags: Optional[List[str]] = ...) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def __enter__(self): ...
    def __exit__(self, _type, _value, _tb) -> None: ...
    def get_default_view(self): ...
    def date_range(self, start_date, num: Any | None = ..., end_date=...): ...
    def is_fixed_time_schedule(self): ...
    def following_schedule(self, dttm): ...
    def previous_schedule(self, dttm): ...
    def get_run_dates(self, start_date, end_date: Any | None = ...): ...
    def normalize_schedule(self, dttm): ...
    def get_last_dagrun(self, session: Any | None = ..., include_externally_triggered: bool = ...): ...
    @property
    def dag_id(self): ...
    @dag_id.setter
    def dag_id(self, value) -> None: ...
    @property
    def full_filepath(self): ...
    @full_filepath.setter
    def full_filepath(self, value) -> None: ...
    @property
    def concurrency(self): ...
    @concurrency.setter
    def concurrency(self, value) -> None: ...
    @property
    def access_control(self): ...
    @access_control.setter
    def access_control(self, value) -> None: ...
    @property
    def description(self): ...
    @property
    def description_unicode(self): ...
    @property
    def pickle_id(self): ...
    @pickle_id.setter
    def pickle_id(self, value) -> None: ...
    @property
    def tasks(self): ...
    @tasks.setter
    def tasks(self, val) -> None: ...
    @property
    def task_ids(self): ...
    @property
    def filepath(self): ...
    @property
    def folder(self): ...
    @property
    def owner(self): ...
    @property
    def allow_future_exec_dates(self): ...
    @property
    def concurrency_reached(self): ...
    @property
    def is_paused(self): ...
    @property
    def normalized_schedule_interval(self) -> Optional[ScheduleInterval]: ...
    def handle_callback(self, dagrun, success: bool = ..., reason: Any | None = ..., session: Any | None = ...) -> None: ...
    def get_active_runs(self): ...
    def get_num_active_runs(self, external_trigger: Any | None = ..., session: Any | None = ...): ...
    def get_dagrun(self, execution_date, session: Any | None = ...): ...
    def get_dagruns_between(self, start_date, end_date, session: Any | None = ...): ...
    @property
    def latest_execution_date(self): ...
    @property
    def subdags(self): ...
    def resolve_template_files(self) -> None: ...
    def get_template_env(self) -> jinja2.Environment: ...
    def set_dependency(self, upstream_task_id, downstream_task_id) -> None: ...
    def get_task_instances(self, start_date: Any | None = ..., end_date: Any | None = ..., state: Any | None = ..., session: Any | None = ...): ...
    @property
    def roots(self): ...
    @property
    def leaves(self): ...
    def topological_sort(self): ...
    def set_dag_runs_state(self, state=..., session: Any | None = ..., start_date: Any | None = ..., end_date: Any | None = ...) -> None: ...
    def clear(self, start_date: Any | None = ..., end_date: Any | None = ..., only_failed: bool = ..., only_running: bool = ..., confirm_prompt: bool = ..., include_subdags: bool = ..., include_parentdag: bool = ..., reset_dag_runs: bool = ..., dry_run: bool = ..., session: Any | None = ..., get_tis: bool = ..., recursion_depth: int = ..., max_recursion_depth: Any | None = ..., dag_bag: Any | None = ...): ...
    @classmethod
    def clear_dags(cls, dags, start_date: Any | None = ..., end_date: Any | None = ..., only_failed: bool = ..., only_running: bool = ..., confirm_prompt: bool = ..., include_subdags: bool = ..., include_parentdag: bool = ..., reset_dag_runs: bool = ..., dry_run: bool = ...): ...
    def __deepcopy__(self, memo): ...
    def sub_dag(self, task_regex, include_downstream: bool = ..., include_upstream: bool = ...): ...
    def has_task(self, task_id): ...
    def get_task(self, task_id): ...
    def pickle_info(self): ...
    last_pickled: Any
    def pickle(self, session: Any | None = ...): ...
    def tree_view(self) -> None: ...
    task_count: Any
    def add_task(self, task) -> None: ...
    def add_tasks(self, tasks) -> None: ...
    def run(self, start_date: Any | None = ..., end_date: Any | None = ..., mark_success: bool = ..., local: bool = ..., executor: Any | None = ..., donot_pickle=..., ignore_task_deps: bool = ..., ignore_first_depends_on_past: bool = ..., pool: Any | None = ..., delay_on_limit_secs: float = ..., verbose: bool = ..., conf: Any | None = ..., rerun_failed_tasks: bool = ..., run_backwards: bool = ...) -> None: ...
    def cli(self) -> None: ...
    def create_dagrun(self, run_id, state, execution_date: Any | None = ..., start_date: Any | None = ..., external_trigger: bool = ..., conf: Any | None = ..., session: Any | None = ...): ...
    def sync_to_db(self, owner: Any | None = ..., sync_time: Any | None = ..., session: Any | None = ...) -> None: ...
    def get_dagtags(self, session: Any | None = ...): ...
    @staticmethod
    def deactivate_unknown_dags(active_dag_ids, session: Any | None = ...) -> None: ...
    @staticmethod
    def deactivate_stale_dags(expiration_date, session: Any | None = ...) -> None: ...
    @staticmethod
    def get_num_task_instances(dag_id, task_ids: Any | None = ..., states: Any | None = ..., session: Any | None = ...): ...
    def test_cycle(self): ...
    @classmethod
    def get_serialized_fields(cls): ...

class DagTag(Base):
    __tablename__: str
    name: Any
    dag_id: Any

class DagModel(Base):
    __tablename__: str
    dag_id: Any
    root_dag_id: Any
    is_paused_at_creation: Any
    is_paused: Any
    is_subdag: Any
    is_active: Any
    last_scheduler_run: Any
    last_pickled: Any
    last_expired: Any
    scheduler_lock: Any
    pickle_id: Any
    fileloc: Any
    owners: Any
    description: Any
    default_view: Any
    schedule_interval: Any
    tags: Any
    __table_args__: Any
    @property
    def timezone(self): ...
    @staticmethod
    def get_dagmodel(dag_id, session: Any | None = ...): ...
    @classmethod
    def get_current(cls, dag_id, session: Any | None = ...): ...
    def get_default_view(self): ...
    def get_last_dagrun(self, session: Any | None = ..., include_externally_triggered: bool = ...): ...
    @staticmethod
    def get_paused_dag_ids(dag_ids, session): ...
    @property
    def safe_dag_id(self): ...
    def get_dag(self, store_serialized_dags: bool = ...): ...
    def create_dagrun(self, run_id, state, execution_date, start_date: Any | None = ..., external_trigger: bool = ..., conf: Any | None = ..., session: Any | None = ...): ...
    def set_is_paused(self, is_paused: bool, including_subdags: bool = ..., store_serialized_dags: bool = ..., session: Any | None = ...) -> None: ...
    @classmethod
    def deactivate_deleted_dags(cls, alive_dag_filelocs, session: Any | None = ...) -> None: ...