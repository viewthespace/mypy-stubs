from airflow.hooks.mssql_hook import MsSqlHook as MsSqlHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class MsSqlOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    mssql_conn_id: Any
    sql: Any
    parameters: Any
    autocommit: Any
    database: Any
    def __init__(self, sql, mssql_conn_id: str = ..., parameters: Any | None = ..., autocommit: bool = ..., database: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
