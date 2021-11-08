from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class BigQueryToBigQueryOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    source_project_dataset_tables: Any
    destination_project_dataset_table: Any
    write_disposition: Any
    create_disposition: Any
    bigquery_conn_id: Any
    delegate_to: Any
    labels: Any
    encryption_configuration: Any
    def __init__(self, source_project_dataset_tables, destination_project_dataset_table, write_disposition: str = ..., create_disposition: str = ..., bigquery_conn_id: str = ..., delegate_to: Any | None = ..., labels: Any | None = ..., encryption_configuration: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
