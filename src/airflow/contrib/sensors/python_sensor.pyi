from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class PythonSensor(BaseSensorOperator):
    template_fields: Any
    python_callable: Any
    op_args: Any
    op_kwargs: Any
    provide_context: Any
    templates_dict: Any
    def __init__(self, python_callable, op_args: Any | None = ..., op_kwargs: Any | None = ..., provide_context: bool = ..., templates_dict: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
