from airflow.hooks.postgres_hook import PostgresHook as PostgresHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class PostgresOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sql: Any
    postgres_conn_id: Any
    autocommit: Any
    parameters: Any
    database: Any
    def __init__(self, sql, postgres_conn_id: str = ..., autocommit: bool = ..., parameters: Any | None = ..., database: Any | None = ..., *args, **kwargs) -> None: ...
    hook: Any
    def execute(self, context) -> None: ...
