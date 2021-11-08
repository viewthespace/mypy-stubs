from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.http_hook import HttpHook as HttpHook
from typing import Any

class DiscordWebhookHook(HttpHook):
    http_conn_id: Any
    webhook_endpoint: Any
    message: Any
    username: Any
    avatar_url: Any
    tts: Any
    proxy: Any
    def __init__(self, http_conn_id: Any | None = ..., webhook_endpoint: Any | None = ..., message: str = ..., username: Any | None = ..., avatar_url: Any | None = ..., tts: bool = ..., proxy: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self) -> None: ...
