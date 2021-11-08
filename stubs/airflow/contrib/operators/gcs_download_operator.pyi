from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.models.xcom import MAX_XCOM_SIZE as MAX_XCOM_SIZE
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GoogleCloudStorageDownloadOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    bucket: Any
    object: Any
    filename: Any
    store_to_xcom_key: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    def __init__(self, bucket, object, filename: Any | None = ..., store_to_xcom_key: Any | None = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
