from airflow.contrib.hooks.segment_hook import SegmentHook as SegmentHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SegmentTrackEventOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    user_id: Any
    event: Any
    properties: Any
    segment_debug_mode: Any
    segment_conn_id: Any
    def __init__(self, user_id, event, properties: Any | None = ..., segment_conn_id: str = ..., segment_debug_mode: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
