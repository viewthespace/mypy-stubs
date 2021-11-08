from airflow.contrib.hooks.ssh_hook import SSHHook as SSHHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SFTPOperation:
    PUT: str
    GET: str

class SFTPOperator(BaseOperator):
    template_fields: Any
    ssh_hook: Any
    ssh_conn_id: Any
    remote_host: Any
    local_filepath: Any
    remote_filepath: Any
    operation: Any
    confirm: Any
    create_intermediate_dirs: Any
    def __init__(self, ssh_hook: Any | None = ..., ssh_conn_id: Any | None = ..., remote_host: Any | None = ..., local_filepath: Any | None = ..., remote_filepath: Any | None = ..., operation=..., confirm: bool = ..., create_intermediate_dirs: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
