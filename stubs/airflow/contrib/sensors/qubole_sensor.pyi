from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class QuboleSensor(BaseSensorOperator):
    template_fields: Any
    template_ext: Any
    data: Any
    qubole_conn_id: Any
    def __init__(self, data, qubole_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...

class QuboleFileSensor(QuboleSensor):
    sensor_class: Any
    def __init__(self, *args, **kwargs) -> None: ...

class QubolePartitionSensor(QuboleSensor):
    sensor_class: Any
    def __init__(self, *args, **kwargs) -> None: ...
