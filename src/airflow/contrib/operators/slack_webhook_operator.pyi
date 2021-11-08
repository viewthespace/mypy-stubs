from airflow.contrib.hooks.slack_webhook_hook import SlackWebhookHook as SlackWebhookHook
from airflow.operators.http_operator import SimpleHttpOperator as SimpleHttpOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SlackWebhookOperator(SimpleHttpOperator):
    template_fields: Any
    http_conn_id: Any
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
    hook: Any
    extra_options: Any
    def __init__(self, http_conn_id: Any | None = ..., webhook_token: Any | None = ..., message: str = ..., attachments: Any | None = ..., blocks: Any | None = ..., channel: Any | None = ..., username: Any | None = ..., icon_emoji: Any | None = ..., icon_url: Any | None = ..., link_names: bool = ..., extra_options: Any | None = ..., proxy: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
