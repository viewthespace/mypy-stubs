from airflow.ti_deps.deps.dag_ti_slots_available_dep import DagTISlotsAvailableDep as DagTISlotsAvailableDep
from airflow.ti_deps.deps.dag_unpaused_dep import DagUnpausedDep as DagUnpausedDep
from airflow.ti_deps.deps.dagrun_exists_dep import DagrunRunningDep as DagrunRunningDep
from airflow.ti_deps.deps.dagrun_id_dep import DagrunIdDep as DagrunIdDep
from airflow.ti_deps.deps.exec_date_after_start_date_dep import ExecDateAfterStartDateDep as ExecDateAfterStartDateDep
from airflow.ti_deps.deps.pool_slots_available_dep import PoolSlotsAvailableDep as PoolSlotsAvailableDep
from airflow.ti_deps.deps.runnable_exec_date_dep import RunnableExecDateDep as RunnableExecDateDep
from airflow.ti_deps.deps.task_concurrency_dep import TaskConcurrencyDep as TaskConcurrencyDep
from airflow.ti_deps.deps.valid_state_dep import ValidStateDep as ValidStateDep
from airflow.utils.state import State as State
from typing import Any

class DepContext:
    deps: Any
    flag_upstream_failed: Any
    ignore_all_deps: Any
    ignore_depends_on_past: Any
    ignore_in_retry_period: Any
    ignore_in_reschedule_period: Any
    ignore_task_deps: Any
    ignore_ti_state: Any
    finished_tasks: Any
    def __init__(self, deps: Any | None = ..., flag_upstream_failed: bool = ..., ignore_all_deps: bool = ..., ignore_depends_on_past: bool = ..., ignore_in_retry_period: bool = ..., ignore_in_reschedule_period: bool = ..., ignore_task_deps: bool = ..., ignore_ti_state: bool = ..., finished_tasks: Any | None = ...) -> None: ...
    def ensure_finished_tasks(self, dag, execution_date, session): ...

SCHEDULEABLE_STATES: Any
RUNNABLE_STATES: Any
QUEUEABLE_STATES: Any
BACKFILL_QUEUEABLE_STATES: Any
SCHEDULED_DEPS: Any
REQUEUEABLE_DEPS: Any
RUNNING_DEPS: Any
BACKFILL_QUEUED_DEPS: Any
SCHEDULER_QUEUED_DEPS: Any
