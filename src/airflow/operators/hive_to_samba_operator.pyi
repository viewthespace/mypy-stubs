from airflow.hooks.hive_hooks import HiveServer2Hook as HiveServer2Hook
from airflow.hooks.samba_hook import SambaHook as SambaHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.operator_helpers import context_to_airflow_vars as context_to_airflow_vars
from typing import Any

class Hive2SambaOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    hiveserver2_conn_id: Any
    samba_conn_id: Any
    destination_filepath: Any
    hql: Any
    def __init__(self, hql, destination_filepath, samba_conn_id: str = ..., hiveserver2_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
