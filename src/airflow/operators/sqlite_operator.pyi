from airflow.hooks.sqlite_hook import SqliteHook as SqliteHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SqliteOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sqlite_conn_id: Any
    sql: Any
    parameters: Any
    def __init__(self, sql, sqlite_conn_id: str = ..., parameters: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
