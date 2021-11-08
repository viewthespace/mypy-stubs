from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class HivePartitionSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    metastore_conn_id: Any
    table: Any
    partition: Any
    schema: Any
    def __init__(self, table, partition: str = ..., metastore_conn_id: str = ..., schema: str = ..., poke_interval=..., *args, **kwargs) -> None: ...
    hook: Any
    def poke(self, context): ...
