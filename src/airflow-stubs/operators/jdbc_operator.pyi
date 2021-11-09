from airflow.hooks.jdbc_hook import JdbcHook as JdbcHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class JdbcOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    parameters: Any
    sql: Any
    jdbc_conn_id: Any
    autocommit: Any
    def __init__(self, sql, jdbc_conn_id: str = ..., autocommit: bool = ..., parameters: Any | None = ..., *args, **kwargs) -> None: ...
    hook: Any
    def execute(self, context) -> None: ...
