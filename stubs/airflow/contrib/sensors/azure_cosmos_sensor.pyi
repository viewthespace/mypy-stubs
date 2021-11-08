from airflow.contrib.hooks.azure_cosmos_hook import AzureCosmosDBHook as AzureCosmosDBHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class AzureCosmosDocumentSensor(BaseSensorOperator):
    template_fields: Any
    azure_cosmos_conn_id: Any
    database_name: Any
    collection_name: Any
    document_id: Any
    def __init__(self, database_name, collection_name, document_id, azure_cosmos_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
