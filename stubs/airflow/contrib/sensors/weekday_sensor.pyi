from airflow.contrib.utils.weekday import WeekDay as WeekDay
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils import timezone as timezone
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class DayOfWeekSensor(BaseSensorOperator):
    week_day: Any
    use_task_execution_day: Any
    def __init__(self, week_day, use_task_execution_day: bool = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
