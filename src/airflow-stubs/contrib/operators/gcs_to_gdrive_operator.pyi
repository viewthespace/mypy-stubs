from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.contrib.hooks.gdrive_hook import GoogleDriveHook as GoogleDriveHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

WILDCARD: str

class GcsToGDriveOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    source_bucket: Any
    source_object: Any
    destination_object: Any
    move_object: Any
    gcp_conn_id: Any
    delegate_to: Any
    gcs_hook: Any
    gdrive_hook: Any
    def __init__(self, source_bucket, source_object, destination_object: Any | None = ..., move_object: bool = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
