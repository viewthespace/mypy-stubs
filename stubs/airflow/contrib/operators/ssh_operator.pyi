from airflow.configuration import conf as conf
from airflow.contrib.hooks.ssh_hook import SSHHook as SSHHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SSHOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ssh_hook: Any
    ssh_conn_id: Any
    remote_host: Any
    command: Any
    timeout: Any
    environment: Any
    do_xcom_push: Any
    get_pty: Any
    def __init__(self, ssh_hook: Any | None = ..., ssh_conn_id: Any | None = ..., remote_host: Any | None = ..., command: Any | None = ..., timeout: int = ..., do_xcom_push: bool = ..., environment: Any | None = ..., get_pty: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
    def tunnel(self) -> None: ...
