from airflow import executors as executors, models as models, settings as settings
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, TaskNotFound as TaskNotFound
from airflow.jobs.base_job import BaseJob as BaseJob
from airflow.models import DagRun as DagRun, SlaMiss as SlaMiss, errors as errors
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.settings import Stats as Stats
from airflow.ti_deps.dep_context import DepContext as DepContext, SCHEDULEABLE_STATES as SCHEDULEABLE_STATES, SCHEDULED_DEPS as SCHEDULED_DEPS
from airflow.ti_deps.deps.pool_slots_available_dep import STATES_TO_COUNT_AS_RUNNING as STATES_TO_COUNT_AS_RUNNING
from airflow.utils import asciiart as asciiart, helpers as helpers, timezone as timezone
from airflow.utils.dag_processing import AbstractDagFileProcessor as AbstractDagFileProcessor, DagFileProcessorAgent as DagFileProcessorAgent, SimpleDag as SimpleDag, SimpleDagBag as SimpleDagBag, SimpleTaskInstance as SimpleTaskInstance, list_py_file_paths as list_py_file_paths
from airflow.utils.db import provide_session as provide_session
from airflow.utils.email import get_email_address_list as get_email_address_list, send_email as send_email
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin, StreamLogWriter as StreamLogWriter, set_context as set_context
from airflow.utils.mixins import MultiprocessingStartMethodMixin as MultiprocessingStartMethodMixin
from airflow.utils.state import State as State
from typing import Any

class DagFileProcessor(AbstractDagFileProcessor, LoggingMixin, MultiprocessingStartMethodMixin):
    class_creation_counter: int
    def __init__(self, file_path, pickle_dags, dag_ids, zombies) -> None: ...
    @property
    def file_path(self): ...
    def start(self) -> None: ...
    def kill(self) -> None: ...
    def terminate(self, sigkill: bool = ...) -> None: ...
    @property
    def pid(self): ...
    @property
    def exit_code(self): ...
    @property
    def done(self): ...
    @property
    def result(self): ...
    @property
    def start_time(self): ...

class SchedulerJob(BaseJob):
    __mapper_args__: Any
    heartrate: Any
    dag_id: Any
    dag_ids: Any
    subdir: Any
    num_runs: Any
    run_duration: Any
    do_pickle: Any
    max_threads: Any
    using_sqlite: bool
    using_mysql: bool
    max_tis_per_query: Any
    processor_agent: Any
    def __init__(self, dag_id: Any | None = ..., dag_ids: Any | None = ..., subdir=..., num_runs=..., processor_poll_interval=..., run_duration: Any | None = ..., do_pickle: bool = ..., log: Any | None = ..., *args, **kwargs) -> None: ...
    def is_alive(self, grace_multiplier: Any | None = ...): ...
    def manage_slas(self, dag, session: Any | None = ...) -> None: ...
    @staticmethod
    def update_import_errors(session, dagbag) -> None: ...
    def create_dag_run(self, dag, session: Any | None = ...): ...
    def process_file(self, file_path, zombies, pickle_dags: bool = ..., session: Any | None = ...): ...
    def heartbeat_callback(self, session: Any | None = ...) -> None: ...
