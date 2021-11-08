from airflow.contrib.operators.sql_to_gcs import BaseSQLToGoogleCloudStorageOperator as BaseSQLToGoogleCloudStorageOperator
from airflow.hooks.postgres_hook import PostgresHook as PostgresHook
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

PY3: Any

class PostgresToGoogleCloudStorageOperator(BaseSQLToGoogleCloudStorageOperator):
    ui_color: str
    type_map: Any
    postgres_conn_id: Any
    def __init__(self, postgres_conn_id: str = ..., *args, **kwargs) -> None: ...
    def query(self): ...
    def field_to_bigquery(self, field): ...
    def convert_type(self, value, schema_type): ...
