from airflow.contrib.hooks.sftp_hook import SFTPHook as SFTPHook
from airflow.operators.sensors import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SFTPSensor(BaseSensorOperator):
    template_fields: Any
    path: Any
    hook: Any
    sftp_conn_id: Any
    def __init__(self, path, sftp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
