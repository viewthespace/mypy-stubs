from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.http_hook import HttpHook as HttpHook
from typing import Any

class SlackWebhookHook(HttpHook):
    webhook_token: Any
    message: Any
    attachments: Any
    blocks: Any
    channel: Any
    username: Any
    icon_emoji: Any
    icon_url: Any
    link_names: Any
    proxy: Any
    extra_options: Any
    def __init__(self, http_conn_id: Any | None = ..., webhook_token: Any | None = ..., message: str = ..., attachments: Any | None = ..., blocks: Any | None = ..., channel: Any | None = ..., username: Any | None = ..., icon_emoji: Any | None = ..., icon_url: Any | None = ..., link_names: bool = ..., proxy: Any | None = ..., extra_options: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self) -> None: ...
