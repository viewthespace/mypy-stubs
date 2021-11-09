from airflow.hooks.hive_hooks import HiveServer2Hook as HiveServer2Hook
from airflow.hooks.mysql_hook import MySqlHook as MySqlHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.operator_helpers import context_to_airflow_vars as context_to_airflow_vars
from typing import Any

class HiveToMySqlTransfer(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sql: Any
    mysql_table: Any
    mysql_conn_id: Any
    mysql_preoperator: Any
    mysql_postoperator: Any
    hiveserver2_conn_id: Any
    bulk_load: Any
    def __init__(self, sql, mysql_table, hiveserver2_conn_id: str = ..., mysql_conn_id: str = ..., mysql_preoperator: Any | None = ..., mysql_postoperator: Any | None = ..., bulk_load: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
