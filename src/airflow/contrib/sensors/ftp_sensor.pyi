from airflow.contrib.hooks.ftp_hook import FTPHook as FTPHook, FTPSHook as FTPSHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class FTPSensor(BaseSensorOperator):
    template_fields: Any
    transient_errors: Any
    error_code_pattern: Any
    path: Any
    ftp_conn_id: Any
    fail_on_transient_errors: Any
    def __init__(self, path, ftp_conn_id: str = ..., fail_on_transient_errors: bool = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...

class FTPSSensor(FTPSensor): ...
