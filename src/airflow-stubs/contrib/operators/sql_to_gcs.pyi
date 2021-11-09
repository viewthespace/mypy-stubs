import abc
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

PY3: Any

class BaseSQLToGoogleCloudStorageOperator(BaseOperator, metaclass=abc.ABCMeta):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sql: Any
    bucket: Any
    filename: Any
    schema_filename: Any
    approx_max_file_size_bytes: Any
    export_format: Any
    field_delimiter: Any
    gzip: Any
    schema: Any
    parameters: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    def __init__(self, sql, bucket, filename, schema_filename: Any | None = ..., approx_max_file_size_bytes: int = ..., export_format: str = ..., field_delimiter: str = ..., gzip: bool = ..., schema: Any | None = ..., parameters: Any | None = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    def convert_types(self, schema, col_type_dict, row): ...
    @abc.abstractmethod
    def query(self): ...
    @abc.abstractmethod
    def field_to_bigquery(self, field): ...
    @abc.abstractmethod
    def convert_type(self, value, schema_type): ...
