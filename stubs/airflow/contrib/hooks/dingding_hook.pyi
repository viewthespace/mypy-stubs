from airflow import AirflowException as AirflowException
from airflow.hooks.http_hook import HttpHook as HttpHook
from typing import Any

class DingdingHook(HttpHook):
    message_type: Any
    message: Any
    at_mobiles: Any
    at_all: Any
    def __init__(self, dingding_conn_id: str = ..., message_type: str = ..., message: Any | None = ..., at_mobiles: Any | None = ..., at_all: bool = ..., *args, **kwargs) -> None: ...
    base_url: Any
    def get_conn(self, headers: Any | None = ...): ...
    def send(self) -> None: ...
