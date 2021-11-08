from airflow.exceptions import AirflowException as AirflowException, AirflowRescheduleException as AirflowRescheduleException, AirflowSensorTimeout as AirflowSensorTimeout, AirflowSkipException as AirflowSkipException
from airflow.models import BaseOperator as BaseOperator, SkipMixin as SkipMixin, TaskReschedule as TaskReschedule
from airflow.ti_deps.deps.ready_to_reschedule import ReadyToRescheduleDep as ReadyToRescheduleDep
from airflow.utils import timezone as timezone
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class BaseSensorOperator(BaseOperator, SkipMixin):
    ui_color: str
    valid_modes: Any
    poke_interval: Any
    soft_fail: Any
    timeout: Any
    mode: Any
    def __init__(self, poke_interval: int = ..., timeout=..., soft_fail: bool = ..., mode: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context) -> None: ...
    def execute(self, context) -> None: ...
    @property
    def reschedule(self): ...
    @property
    def deps(self): ...
