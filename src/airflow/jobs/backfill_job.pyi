from airflow import executors as executors, models as models
from airflow.exceptions import AirflowException as AirflowException, DagConcurrencyLimitReached as DagConcurrencyLimitReached, NoAvailablePoolSlot as NoAvailablePoolSlot, PoolNotFound as PoolNotFound, TaskConcurrencyLimitReached as TaskConcurrencyLimitReached
from airflow.jobs.base_job import BaseJob as BaseJob
from airflow.models import DAG as DAG, DagPickle as DagPickle, DagRun as DagRun
from airflow.ti_deps.dep_context import BACKFILL_QUEUED_DEPS as BACKFILL_QUEUED_DEPS, DepContext as DepContext
from airflow.utils import timezone as timezone
from airflow.utils.configuration import tmp_configuration_copy as tmp_configuration_copy
from airflow.utils.db import provide_session as provide_session
from airflow.utils.state import State as State
from typing import Any

class BackfillJob(BaseJob):
    ID_PREFIX: str
    ID_FORMAT_PREFIX: Any
    STATES_COUNT_AS_RUNNING: Any
    __mapper_args__: Any
    class _DagRunTaskStatus:
        to_run: Any
        running: Any
        skipped: Any
        succeeded: Any
        failed: Any
        not_ready: Any
        deadlocked: Any
        active_runs: Any
        executed_dag_run_dates: Any
        finished_runs: Any
        total_runs: Any
        def __init__(self, to_run: Any | None = ..., running: Any | None = ..., skipped: Any | None = ..., succeeded: Any | None = ..., failed: Any | None = ..., not_ready: Any | None = ..., deadlocked: Any | None = ..., active_runs: Any | None = ..., executed_dag_run_dates: Any | None = ..., finished_runs: int = ..., total_runs: int = ...) -> None: ...
    dag: Any
    dag_id: Any
    bf_start_date: Any
    bf_end_date: Any
    mark_success: Any
    donot_pickle: Any
    ignore_first_depends_on_past: Any
    ignore_task_deps: Any
    pool: Any
    delay_on_limit_secs: Any
    verbose: Any
    conf: Any
    rerun_failed_tasks: Any
    run_backwards: Any
    def __init__(self, dag, start_date: Any | None = ..., end_date: Any | None = ..., mark_success: bool = ..., donot_pickle: bool = ..., ignore_first_depends_on_past: bool = ..., ignore_task_deps: bool = ..., pool: Any | None = ..., delay_on_limit_secs: float = ..., verbose: bool = ..., conf: Any | None = ..., rerun_failed_tasks: bool = ..., run_backwards: bool = ..., *args, **kwargs) -> None: ...
