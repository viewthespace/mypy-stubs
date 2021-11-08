from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any, Iterable

class GoogleCloudStorageListOperator(BaseOperator):
    template_fields: Iterable[str]
    ui_color: str
    bucket: Any
    prefix: Any
    delimiter: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    def __init__(self, bucket, prefix: Any | None = ..., delimiter: Any | None = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
