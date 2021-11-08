from airflow.contrib.hooks.azure_data_lake_hook import AzureDataLakeHook as AzureDataLakeHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any, Iterable

class AzureDataLakeStorageListOperator(BaseOperator):
    template_fields: Iterable[str]
    ui_color: str
    path: Any
    azure_data_lake_conn_id: Any
    def __init__(self, path, azure_data_lake_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
