from airflow.contrib.hooks.vertica_hook import VerticaHook as VerticaHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class VerticaOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    vertica_conn_id: Any
    sql: Any
    def __init__(self, sql, vertica_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
