from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.contrib.operators.gcs_list_operator import GoogleCloudStorageListOperator as GoogleCloudStorageListOperator
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GoogleCloudStorageToS3Operator(GoogleCloudStorageListOperator):
    template_fields: Any
    ui_color: str
    dest_aws_conn_id: Any
    dest_s3_key: Any
    dest_verify: Any
    replace: Any
    def __init__(self, bucket, prefix: Any | None = ..., delimiter: Any | None = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., dest_aws_conn_id: Any | None = ..., dest_s3_key: Any | None = ..., dest_verify: Any | None = ..., replace: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
