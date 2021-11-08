from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.slack_hook import SlackHook as SlackHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SlackAPIOperator(BaseOperator):
    token: Any
    slack_conn_id: Any
    method: Any
    api_params: Any
    def __init__(self, slack_conn_id: Any | None = ..., token: Any | None = ..., method: Any | None = ..., api_params: Any | None = ..., *args, **kwargs) -> None: ...
    def construct_api_call_params(self) -> None: ...
    def execute(self, **kwargs) -> None: ...

class SlackAPIPostOperator(SlackAPIOperator):
    template_fields: Any
    ui_color: str
    method: str
    channel: Any
    username: Any
    text: Any
    icon_url: Any
    attachments: Any
    blocks: Any
    def __init__(self, channel: str = ..., username: str = ..., text: str = ..., icon_url: str = ..., attachments: Any | None = ..., blocks: Any | None = ..., *args, **kwargs) -> None: ...
    api_params: Any
    def construct_api_call_params(self) -> None: ...
