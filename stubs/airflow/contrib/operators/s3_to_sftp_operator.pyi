from airflow.contrib.hooks.ssh_hook import SSHHook as SSHHook
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class S3ToSFTPOperator(BaseOperator):
    template_fields: Any
    sftp_conn_id: Any
    sftp_path: Any
    s3_bucket: Any
    s3_key: Any
    s3_conn_id: Any
    def __init__(self, s3_bucket, s3_key, sftp_path, sftp_conn_id: str = ..., s3_conn_id: str = ..., *args, **kwargs) -> None: ...
    @staticmethod
    def get_s3_key(s3_key): ...
    def execute(self, context) -> None: ...
