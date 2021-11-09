from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class BigQueryToCloudStorageOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    source_project_dataset_table: Any
    destination_cloud_storage_uris: Any
    compression: Any
    export_format: Any
    field_delimiter: Any
    print_header: Any
    bigquery_conn_id: Any
    delegate_to: Any
    labels: Any
    def __init__(self, source_project_dataset_table, destination_cloud_storage_uris, compression: str = ..., export_format: str = ..., field_delimiter: str = ..., print_header: bool = ..., bigquery_conn_id: str = ..., delegate_to: Any | None = ..., labels: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
