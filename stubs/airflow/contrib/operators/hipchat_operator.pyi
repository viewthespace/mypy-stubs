from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class HipChatAPIOperator(BaseOperator):
    token: Any
    base_url: Any
    method: Any
    url: Any
    body: Any
    def __init__(self, token, base_url: str = ..., *args, **kwargs) -> None: ...
    def prepare_request(self) -> None: ...
    def execute(self, context) -> None: ...

class HipChatAPISendRoomNotificationOperator(HipChatAPIOperator):
    template_fields: Any
    ui_color: str
    room_id: Any
    message: Any
    def __init__(self, room_id, message, *args, **kwargs) -> None: ...
    method: str
    url: Any
    body: Any
    def prepare_request(self) -> None: ...
