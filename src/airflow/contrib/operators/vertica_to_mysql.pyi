from airflow.contrib.hooks.vertica_hook import VerticaHook as VerticaHook
from airflow.hooks.mysql_hook import MySqlHook as MySqlHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class VerticaToMySqlTransfer(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sql: Any
    mysql_table: Any
    mysql_conn_id: Any
    mysql_preoperator: Any
    mysql_postoperator: Any
    vertica_conn_id: Any
    bulk_load: Any
    def __init__(self, sql, mysql_table, vertica_conn_id: str = ..., mysql_conn_id: str = ..., mysql_preoperator: Any | None = ..., mysql_postoperator: Any | None = ..., bulk_load: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
