from airflow.contrib.hooks.dingding_hook import DingdingHook as DingdingHook
from airflow.operators.bash_operator import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class DingdingOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    dingding_conn_id: Any
    message_type: Any
    message: Any
    at_mobiles: Any
    at_all: Any
    def __init__(self, dingding_conn_id: str = ..., message_type: str = ..., message: Any | None = ..., at_mobiles: Any | None = ..., at_all: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
