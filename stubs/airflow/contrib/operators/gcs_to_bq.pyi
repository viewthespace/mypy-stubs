from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GoogleCloudStorageToBigQueryOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    bucket: Any
    source_objects: Any
    schema_object: Any
    destination_project_dataset_table: Any
    schema_fields: Any
    source_format: Any
    compression: Any
    create_disposition: Any
    skip_leading_rows: Any
    write_disposition: Any
    field_delimiter: Any
    max_bad_records: Any
    quote_character: Any
    ignore_unknown_values: Any
    allow_quoted_newlines: Any
    allow_jagged_rows: Any
    external_table: Any
    encoding: Any
    max_id_key: Any
    bigquery_conn_id: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    schema_update_options: Any
    src_fmt_configs: Any
    time_partitioning: Any
    cluster_fields: Any
    autodetect: Any
    encryption_configuration: Any
    def __init__(self, bucket, source_objects, destination_project_dataset_table, schema_fields: Any | None = ..., schema_object: Any | None = ..., source_format: str = ..., compression: str = ..., create_disposition: str = ..., skip_leading_rows: int = ..., write_disposition: str = ..., field_delimiter: str = ..., max_bad_records: int = ..., quote_character: Any | None = ..., ignore_unknown_values: bool = ..., allow_quoted_newlines: bool = ..., allow_jagged_rows: bool = ..., encoding: str = ..., max_id_key: Any | None = ..., bigquery_conn_id: str = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., schema_update_options=..., src_fmt_configs: Any | None = ..., external_table: bool = ..., time_partitioning: Any | None = ..., cluster_fields: Any | None = ..., autodetect: bool = ..., encryption_configuration: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
