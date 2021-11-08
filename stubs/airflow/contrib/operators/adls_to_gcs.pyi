from airflow.contrib.hooks.azure_data_lake_hook import AzureDataLakeHook as AzureDataLakeHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.contrib.operators.adls_list_operator import AzureDataLakeStorageListOperator as AzureDataLakeStorageListOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class AdlsToGoogleCloudStorageOperator(AzureDataLakeStorageListOperator):
    template_fields: Any
    ui_color: str
    src_adls: Any
    dest_gcs: Any
    replace: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    gzip: Any
    def __init__(self, src_adls, dest_gcs, azure_data_lake_conn_id, google_cloud_storage_conn_id, delegate_to: Any | None = ..., replace: bool = ..., gzip: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
