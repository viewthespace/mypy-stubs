from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.version import version as version
from typing import Any

class GoogleCloudStorageCreateBucketOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    bucket_name: Any
    resource: Any
    storage_class: Any
    location: Any
    project_id: Any
    labels: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    def __init__(self, bucket_name, resource: Any | None = ..., storage_class: str = ..., location: str = ..., project_id: Any | None = ..., labels: Any | None = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
