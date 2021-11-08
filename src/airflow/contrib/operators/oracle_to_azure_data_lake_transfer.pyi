from airflow.contrib.hooks.azure_data_lake_hook import AzureDataLakeHook as AzureDataLakeHook
from airflow.hooks.oracle_hook import OracleHook as OracleHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.file import TemporaryDirectory as TemporaryDirectory
from typing import Any

class OracleToAzureDataLakeTransfer(BaseOperator):
    template_fields: Any
    ui_color: str
    filename: Any
    oracle_conn_id: Any
    sql: Any
    sql_params: Any
    azure_data_lake_conn_id: Any
    azure_data_lake_path: Any
    delimiter: Any
    encoding: Any
    quotechar: Any
    quoting: Any
    def __init__(self, filename, azure_data_lake_conn_id, azure_data_lake_path, oracle_conn_id, sql, sql_params: Any | None = ..., delimiter: str = ..., encoding: str = ..., quotechar: str = ..., quoting=..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
