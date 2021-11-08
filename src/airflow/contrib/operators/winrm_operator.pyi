from airflow.configuration import conf as conf
from airflow.contrib.hooks.winrm_hook import WinRMHook as WinRMHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class WinRMOperator(BaseOperator):
    template_fields: Any
    winrm_hook: Any
    ssh_conn_id: Any
    remote_host: Any
    command: Any
    timeout: Any
    do_xcom_push: Any
    def __init__(self, winrm_hook: Any | None = ..., ssh_conn_id: Any | None = ..., remote_host: Any | None = ..., command: Any | None = ..., timeout: int = ..., do_xcom_push: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
