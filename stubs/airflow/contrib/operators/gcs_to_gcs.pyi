from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

WILDCARD: str

class GoogleCloudStorageToGoogleCloudStorageOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    source_bucket: Any
    source_object: Any
    destination_bucket: Any
    destination_object: Any
    move_object: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    last_modified_time: Any
    def __init__(self, source_bucket, source_object, destination_bucket: Any | None = ..., destination_object: Any | None = ..., move_object: bool = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., last_modified_time: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
