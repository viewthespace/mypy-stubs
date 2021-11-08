from airflow.contrib.hooks.cassandra_hook import CassandraHook as CassandraHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class CassandraToGoogleCloudStorageOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    cql: Any
    bucket: Any
    filename: Any
    schema_filename: Any
    approx_max_file_size_bytes: Any
    cassandra_conn_id: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    gzip: Any
    hook: Any
    def __init__(self, cql, bucket, filename, schema_filename: Any | None = ..., approx_max_file_size_bytes: int = ..., gzip: bool = ..., cassandra_conn_id: str = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    CQL_TYPE_MAP: Any
    def execute(self, context) -> None: ...
    @classmethod
    def generate_data_dict(cls, names, values): ...
    @classmethod
    def convert_value(cls, name, value): ...
    @classmethod
    def convert_array_types(cls, name, value): ...
    @classmethod
    def convert_user_type(cls, name, value): ...
    @classmethod
    def convert_tuple_type(cls, name, value): ...
    @classmethod
    def convert_map_type(cls, name, value): ...
    @classmethod
    def generate_schema_dict(cls, name, type): ...
    @classmethod
    def get_bq_fields(cls, name, type): ...
    @classmethod
    def is_simple_type(cls, type): ...
    @classmethod
    def is_array_type(cls, type): ...
    @classmethod
    def is_record_type(cls, type): ...
    @classmethod
    def get_bq_type(cls, type): ...
    @classmethod
    def get_bq_mode(cls, type): ...
