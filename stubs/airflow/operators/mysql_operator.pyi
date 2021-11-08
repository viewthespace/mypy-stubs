from airflow.hooks.mysql_hook import MySqlHook as MySqlHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class MySqlOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    mysql_conn_id: Any
    sql: Any
    autocommit: Any
    parameters: Any
    database: Any
    def __init__(self, sql, mysql_conn_id: str = ..., parameters: Any | None = ..., autocommit: bool = ..., database: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
