from airflow.contrib.hooks.snowflake_hook import SnowflakeHook as SnowflakeHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SnowflakeOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    snowflake_conn_id: Any
    sql: Any
    autocommit: Any
    parameters: Any
    warehouse: Any
    database: Any
    role: Any
    schema: Any
    authenticator: Any
    def __init__(self, sql, snowflake_conn_id: str = ..., parameters: Any | None = ..., autocommit: bool = ..., warehouse: Any | None = ..., database: Any | None = ..., role: Any | None = ..., schema: Any | None = ..., authenticator: Any | None = ..., *args, **kwargs) -> None: ...
    def get_hook(self): ...
    def execute(self, context) -> None: ...
