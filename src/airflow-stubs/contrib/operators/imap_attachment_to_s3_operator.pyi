from airflow.contrib.hooks.imap_hook import ImapHook as ImapHook
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class ImapAttachmentToS3Operator(BaseOperator):
    template_fields: Any
    imap_attachment_name: Any
    s3_key: Any
    imap_mail_folder: Any
    imap_check_regex: Any
    s3_overwrite: Any
    imap_conn_id: Any
    s3_conn_id: Any
    def __init__(self, imap_attachment_name, s3_key, imap_mail_folder: str = ..., imap_check_regex: bool = ..., s3_overwrite: bool = ..., imap_conn_id: str = ..., s3_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
