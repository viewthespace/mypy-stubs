from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.http_hook import HttpHook as HttpHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SimpleHttpOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    http_conn_id: Any
    method: Any
    endpoint: Any
    headers: Any
    data: Any
    response_check: Any
    extra_options: Any
    xcom_push_flag: Any
    log_response: Any
    def __init__(self, endpoint, method: str = ..., data: Any | None = ..., headers: Any | None = ..., response_check: Any | None = ..., extra_options: Any | None = ..., xcom_push: bool = ..., http_conn_id: str = ..., log_response: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
