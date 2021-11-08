from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class BigQueryGetDataOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    dataset_id: Any
    table_id: Any
    max_results: Any
    selected_fields: Any
    bigquery_conn_id: Any
    delegate_to: Any
    def __init__(self, dataset_id, table_id, max_results: int = ..., selected_fields: Any | None = ..., bigquery_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
