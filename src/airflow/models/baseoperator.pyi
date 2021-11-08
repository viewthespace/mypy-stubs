import abc
import jinja2
from abc import abstractmethod
from airflow import settings as settings
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.lineage import DataSet as DataSet, apply_lineage as apply_lineage, prepare_lineage as prepare_lineage
from airflow.models.dag import DAG as DAG
from airflow.models.pool import Pool as Pool
from airflow.models.taskinstance import TaskInstance as TaskInstance, clear_task_instances as clear_task_instances
from airflow.models.xcom import XCOM_RETURN_KEY as XCOM_RETURN_KEY
from airflow.ti_deps.deps.not_in_retry_period_dep import NotInRetryPeriodDep as NotInRetryPeriodDep
from airflow.ti_deps.deps.not_previously_skipped_dep import NotPreviouslySkippedDep as NotPreviouslySkippedDep
from airflow.ti_deps.deps.prev_dagrun_dep import PrevDagrunDep as PrevDagrunDep
from airflow.ti_deps.deps.trigger_rule_dep import TriggerRuleDep as TriggerRuleDep
from airflow.utils import timezone as timezone
from airflow.utils.db import provide_session as provide_session
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.helpers import validate_key as validate_key
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.operator_resources import Resources as Resources
from airflow.utils.trigger_rule import TriggerRule as TriggerRule
from airflow.utils.weight_rule import WeightRule as WeightRule
from datetime import datetime, timedelta
from typing import Any, Callable, ClassVar, Dict, Iterable, List, Optional, Set, Type, Union

class BaseOperator(LoggingMixin):
    template_fields: Iterable[str]
    template_ext: Iterable[str]
    ui_color: str
    ui_fgcolor: str
    pool: str
    shallow_copy_attrs: Iterable[str]
    operator_extra_links: Iterable[BaseOperatorLink]
    task_id: Any
    owner: Any
    email: Any
    email_on_retry: Any
    email_on_failure: Any
    start_date: Any
    end_date: Any
    trigger_rule: Any
    depends_on_past: Any
    wait_for_downstream: Any
    retries: Any
    queue: Any
    pool_slots: Any
    sla: Any
    execution_timeout: Any
    on_failure_callback: Any
    on_success_callback: Any
    on_retry_callback: Any
    retry_delay: Any
    retry_exponential_backoff: Any
    max_retry_delay: Any
    params: Any
    priority_weight: Any
    weight_rule: Any
    resources: Any
    run_as_user: Any
    task_concurrency: Any
    executor_config: Any
    do_xcom_push: Any
    subdag: Any
    inlets: Any
    outlets: Any
    lineage_data: Any
    def __init__(self, task_id: str, owner: str = ..., email: Optional[Union[str, Iterable[str]]] = ..., email_on_retry: bool = ..., email_on_failure: bool = ..., retries: int = ..., retry_delay: timedelta = ..., retry_exponential_backoff: bool = ..., max_retry_delay: Optional[datetime] = ..., start_date: Optional[datetime] = ..., end_date: Optional[datetime] = ..., schedule_interval: Any | None = ..., depends_on_past: bool = ..., wait_for_downstream: bool = ..., dag: Optional[DAG] = ..., params: Optional[Dict] = ..., default_args: Optional[Dict] = ..., priority_weight: int = ..., weight_rule: str = ..., queue: str = ..., pool: str = ..., pool_slots: int = ..., sla: Optional[timedelta] = ..., execution_timeout: Optional[timedelta] = ..., on_failure_callback: Optional[Callable] = ..., on_success_callback: Optional[Callable] = ..., on_retry_callback: Optional[Callable] = ..., trigger_rule: str = ..., resources: Optional[Dict] = ..., run_as_user: Optional[str] = ..., task_concurrency: Optional[int] = ..., executor_config: Optional[Dict] = ..., do_xcom_push: bool = ..., inlets: Optional[Dict] = ..., outlets: Optional[Dict] = ..., *args, **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def __rshift__(self, other): ...
    def __lshift__(self, other): ...
    def __rrshift__(self, other): ...
    def __rlshift__(self, other): ...
    @property
    def dag(self): ...
    @dag.setter
    def dag(self, dag) -> None: ...
    def has_dag(self): ...
    @property
    def dag_id(self): ...
    @property
    def deps(self): ...
    @property
    def schedule_interval(self): ...
    @property
    def priority_weight_total(self): ...
    def operator_extra_link_dict(self): ...
    def global_operator_extra_link_dict(self): ...
    def pre_execute(self, context) -> None: ...
    def execute(self, context) -> None: ...
    def post_execute(self, context, result: Any | None = ...) -> None: ...
    def on_kill(self) -> None: ...
    def __deepcopy__(self, memo): ...
    def render_template_fields(self, context: Dict, jinja_env: Optional[jinja2.Environment] = ...) -> None: ...
    def render_template(self, content: Any, context: Dict, jinja_env: Optional[jinja2.Environment] = ..., seen_oids: Optional[Set] = ...) -> Any: ...
    def get_template_env(self) -> jinja2.Environment: ...
    def prepare_template(self) -> None: ...
    def resolve_template_files(self) -> None: ...
    @property
    def upstream_list(self): ...
    @property
    def upstream_task_ids(self): ...
    @property
    def downstream_list(self): ...
    @property
    def downstream_task_ids(self): ...
    def clear(self, start_date: Any | None = ..., end_date: Any | None = ..., upstream: bool = ..., downstream: bool = ..., session: Any | None = ...): ...
    def get_task_instances(self, start_date: Any | None = ..., end_date: Any | None = ..., session: Any | None = ...): ...
    def get_flat_relative_ids(self, upstream: bool = ..., found_descendants: Any | None = ...): ...
    def get_flat_relatives(self, upstream: bool = ...): ...
    def run(self, start_date: Any | None = ..., end_date: Any | None = ..., ignore_first_depends_on_past: bool = ..., ignore_ti_state: bool = ..., mark_success: bool = ...) -> None: ...
    def dry_run(self) -> None: ...
    def get_direct_relative_ids(self, upstream: bool = ...): ...
    def get_direct_relatives(self, upstream: bool = ...): ...
    @property
    def task_type(self): ...
    def add_only_new(self, item_set, item) -> None: ...
    def set_downstream(self, task_or_task_list) -> None: ...
    def set_upstream(self, task_or_task_list) -> None: ...
    def xcom_push(self, context, key, value, execution_date: Any | None = ...) -> None: ...
    def xcom_pull(self, context, task_ids: Any | None = ..., dag_id: Any | None = ..., key=..., include_prior_dates: Any | None = ...): ...
    def extra_links(self): ...
    def get_extra_links(self, dttm, link_name): ...
    @classmethod
    def get_serialized_fields(cls): ...

class BaseOperatorLink(metaclass=abc.ABCMeta):
    __metaclass__: Any
    operators: ClassVar[List[Type[BaseOperator]]]
    @property
    @abstractmethod
    def name(self) -> str: ...
    @abstractmethod
    def get_link(self, operator: BaseOperator, dttm: datetime) -> str: ...
    def __init__(self) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...