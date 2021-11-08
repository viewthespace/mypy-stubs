from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.contrib.operators.s3_list_operator import S3ListOperator as S3ListOperator
from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class S3ToGoogleCloudStorageOperator(S3ListOperator):
    template_fields: Any
    ui_color: str
    dest_gcs_conn_id: Any
    dest_gcs: Any
    delegate_to: Any
    replace: Any
    verify: Any
    gzip: Any
    def __init__(self, bucket, prefix: str = ..., delimiter: str = ..., aws_conn_id: str = ..., verify: Any | None = ..., dest_gcs_conn_id: Any | None = ..., dest_gcs: Any | None = ..., delegate_to: Any | None = ..., replace: bool = ..., gzip: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
