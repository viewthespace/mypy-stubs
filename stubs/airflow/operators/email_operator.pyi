from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.email import send_email as send_email
from typing import Any

class EmailOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    to: Any
    subject: Any
    html_content: Any
    files: Any
    cc: Any
    bcc: Any
    mime_subtype: Any
    mime_charset: Any
    def __init__(self, to, subject, html_content, files: Any | None = ..., cc: Any | None = ..., bcc: Any | None = ..., mime_subtype: str = ..., mime_charset: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
