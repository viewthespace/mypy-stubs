from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class AwsGlueCatalogPartitionSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    aws_conn_id: Any
    region_name: Any
    table_name: Any
    expression: Any
    database_name: Any
    def __init__(self, table_name, expression: str = ..., aws_conn_id: str = ..., region_name: Any | None = ..., database_name: str = ..., poke_interval=..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
    hook: Any
    def get_hook(self): ...
