from airflow.contrib.hooks.discord_webhook_hook import DiscordWebhookHook as DiscordWebhookHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.operators.http_operator import SimpleHttpOperator as SimpleHttpOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class DiscordWebhookOperator(SimpleHttpOperator):
    template_fields: Any
    http_conn_id: Any
    webhook_endpoint: Any
    message: Any
    username: Any
    avatar_url: Any
    tts: Any
    proxy: Any
    hook: Any
    def __init__(self, http_conn_id: Any | None = ..., webhook_endpoint: Any | None = ..., message: str = ..., username: Any | None = ..., avatar_url: Any | None = ..., tts: bool = ..., proxy: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
