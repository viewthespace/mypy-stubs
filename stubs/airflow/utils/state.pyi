from airflow.settings import STATE_COLORS as STATE_COLORS
from typing import Any

class State:
    NONE: Any
    REMOVED: str
    SCHEDULED: str
    QUEUED: str
    RUNNING: str
    SUCCESS: str
    SHUTDOWN: str
    FAILED: str
    UP_FOR_RETRY: str
    UP_FOR_RESCHEDULE: str
    UPSTREAM_FAILED: str
    SKIPPED: str
    task_states: Any
    dag_states: Any
    state_color: Any
    @classmethod
    def color(cls, state): ...
    @classmethod
    def color_fg(cls, state): ...
    @classmethod
    def finished(cls): ...
    @classmethod
    def unfinished(cls): ...
