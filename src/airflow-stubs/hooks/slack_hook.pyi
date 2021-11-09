from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class SlackHook(BaseHook):
    token: Any
    def __init__(self, token: Any | None = ..., slack_conn_id: Any | None = ...) -> None: ...
    def call(self, method, api_params) -> None: ...
