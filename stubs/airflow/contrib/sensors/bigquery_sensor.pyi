from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class BigQueryTableSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    project_id: Any
    dataset_id: Any
    table_id: Any
    bigquery_conn_id: Any
    delegate_to: Any
    def __init__(self, project_id, dataset_id, table_id, bigquery_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
