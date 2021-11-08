from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class SegmentHook(BaseHook):
    segment_conn_id: Any
    segment_debug_mode: Any
    connection: Any
    extras: Any
    write_key: Any
    def __init__(self, segment_conn_id: str = ..., segment_debug_mode: bool = ..., *args, **kwargs) -> None: ...
    def get_conn(self): ...
    def on_error(self, error, items) -> None: ...
