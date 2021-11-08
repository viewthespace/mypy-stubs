from airflow.contrib.operators.sql_to_gcs import BaseSQLToGoogleCloudStorageOperator as BaseSQLToGoogleCloudStorageOperator
from airflow.hooks.mysql_hook import MySqlHook as MySqlHook
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

PY3: Any

class MySqlToGoogleCloudStorageOperator(BaseSQLToGoogleCloudStorageOperator):
    ui_color: str
    type_map: Any
    mysql_conn_id: Any
    ensure_utc: Any
    def __init__(self, mysql_conn_id: str = ..., ensure_utc: bool = ..., *args, **kwargs) -> None: ...
    def query(self): ...
    def field_to_bigquery(self, field): ...
    def convert_type(self, value, schema_type): ...
