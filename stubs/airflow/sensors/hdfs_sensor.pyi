from airflow import settings as settings
from airflow.hooks.hdfs_hook import HDFSHook as HDFSHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

log: Any

class HdfsSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: Any
    filepath: Any
    hdfs_conn_id: Any
    file_size: Any
    ignored_ext: Any
    ignore_copying: Any
    hook: Any
    def __init__(self, filepath, hdfs_conn_id: str = ..., ignored_ext: Any | None = ..., ignore_copying: bool = ..., file_size: Any | None = ..., hook=..., *args, **kwargs) -> None: ...
    @staticmethod
    def filter_for_filesize(result, size: Any | None = ...): ...
    @staticmethod
    def filter_for_ignored_ext(result, ignored_ext, ignore_copying): ...
    def poke(self, context): ...
