from airflow.contrib.hooks.wasb_hook import WasbHook as WasbHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class WasbBlobSensor(BaseSensorOperator):
    template_fields: Any
    wasb_conn_id: Any
    container_name: Any
    blob_name: Any
    check_options: Any
    def __init__(self, container_name, blob_name, wasb_conn_id: str = ..., check_options: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...

class WasbPrefixSensor(BaseSensorOperator):
    template_fields: Any
    wasb_conn_id: Any
    container_name: Any
    prefix: Any
    check_options: Any
    def __init__(self, container_name, prefix, wasb_conn_id: str = ..., check_options: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
