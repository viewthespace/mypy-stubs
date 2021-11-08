from airflow.contrib.operators.sql_to_gcs import BaseSQLToGoogleCloudStorageOperator as BaseSQLToGoogleCloudStorageOperator
from airflow.hooks.mssql_hook import MsSqlHook as MsSqlHook
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class MsSqlToGoogleCloudStorageOperator(BaseSQLToGoogleCloudStorageOperator):
    ui_color: str
    type_map: Any
    mssql_conn_id: Any
    def __init__(self, mssql_conn_id: str = ..., *args, **kwargs) -> None: ...
    def query(self): ...
    def field_to_bigquery(self, field): ...
    @classmethod
    def convert_type(cls, value, schema_type): ...
