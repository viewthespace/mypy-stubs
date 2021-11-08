from airflow.utils.email import get_email_address_list as get_email_address_list
from typing import Any

log: Any

def send_email(to, subject, html_content, files: Any | None = ..., dryrun: bool = ..., cc: Any | None = ..., bcc: Any | None = ..., mime_subtype: str = ..., **kwargs) -> None: ...
