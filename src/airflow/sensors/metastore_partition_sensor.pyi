from airflow.sensors.sql_sensor import SqlSensor as SqlSensor
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class MetastorePartitionSensor(SqlSensor):
    template_fields: Any
    ui_color: str
    partition_name: Any
    table: Any
    schema: Any
    first_poke: bool
    conn_id: Any
    def __init__(self, table, partition_name, schema: str = ..., mysql_conn_id: str = ..., *args, **kwargs) -> None: ...
    sql: Any
    def poke(self, context): ...
