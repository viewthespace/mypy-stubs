from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GoogleCloudStorageDeleteOperator(BaseOperator):
    template_fields: Any
    bucket_name: Any
    objects: Any
    prefix: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    def __init__(self, bucket_name, objects: Any | None = ..., prefix: Any | None = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
