from airflow.hooks.hive_hooks import HiveCliHook as HiveCliHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils import operator_helpers as operator_helpers
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.operator_helpers import context_to_airflow_vars as context_to_airflow_vars
from typing import Any

class HiveOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    hql: Any
    hive_cli_conn_id: Any
    schema: Any
    hiveconfs: Any
    hiveconf_jinja_translate: Any
    script_begin_tag: Any
    run_as: Any
    mapred_queue: Any
    mapred_queue_priority: Any
    mapred_job_name: Any
    hook: Any
    def __init__(self, hql, hive_cli_conn_id: str = ..., schema: str = ..., hiveconfs: Any | None = ..., hiveconf_jinja_translate: bool = ..., script_begin_tag: Any | None = ..., run_as_owner: bool = ..., mapred_queue: Any | None = ..., mapred_queue_priority: Any | None = ..., mapred_job_name: Any | None = ..., *args, **kwargs) -> None: ...
    def get_hook(self): ...
    def prepare_template(self) -> None: ...
    def execute(self, context) -> None: ...
    def dry_run(self) -> None: ...
    def on_kill(self) -> None: ...
    def clear_airflow_vars(self) -> None: ...
