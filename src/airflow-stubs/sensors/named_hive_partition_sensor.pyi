from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class NamedHivePartitionSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    metastore_conn_id: Any
    partition_names: Any
    hook: Any
    def __init__(self, partition_names, metastore_conn_id: str = ..., poke_interval=..., hook: Any | None = ..., *args, **kwargs) -> None: ...
    @staticmethod
    def parse_partition_name(partition): ...
    def poke_partition(self, partition): ...
    def poke(self, context): ...
