from airflow.hooks.mysql_hook import MySqlHook as MySqlHook
from airflow.hooks.presto_hook import PrestoHook as PrestoHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class PrestoToMySqlTransfer(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sql: Any
    mysql_table: Any
    mysql_conn_id: Any
    mysql_preoperator: Any
    presto_conn_id: Any
    def __init__(self, sql, mysql_table, presto_conn_id: str = ..., mysql_conn_id: str = ..., mysql_preoperator: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
