from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class FileToGoogleCloudStorageOperator(BaseOperator):
    template_fields: Any
    src: Any
    dst: Any
    bucket: Any
    google_cloud_storage_conn_id: Any
    mime_type: Any
    delegate_to: Any
    gzip: Any
    def __init__(self, src, dst, bucket, google_cloud_storage_conn_id: str = ..., mime_type: str = ..., delegate_to: Any | None = ..., gzip: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
