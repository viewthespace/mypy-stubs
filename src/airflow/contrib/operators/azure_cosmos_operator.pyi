from airflow.contrib.hooks.azure_cosmos_hook import AzureCosmosDBHook as AzureCosmosDBHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class AzureCosmosInsertDocumentOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    database_name: Any
    collection_name: Any
    document: Any
    azure_cosmos_conn_id: Any
    def __init__(self, database_name, collection_name, document, azure_cosmos_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
