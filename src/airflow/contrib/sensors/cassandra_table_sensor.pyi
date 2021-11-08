from airflow.contrib.hooks.cassandra_hook import CassandraHook as CassandraHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class CassandraTableSensor(BaseSensorOperator):
    template_fields: Any
    cassandra_conn_id: Any
    table: Any
    def __init__(self, table, cassandra_conn_id, *args, **kwargs) -> None: ...
    def poke(self, context): ...
