from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class BigQueryTableDeleteOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    deletion_dataset_table: Any
    bigquery_conn_id: Any
    delegate_to: Any
    ignore_if_missing: Any
    def __init__(self, deletion_dataset_table, bigquery_conn_id: str = ..., delegate_to: Any | None = ..., ignore_if_missing: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
