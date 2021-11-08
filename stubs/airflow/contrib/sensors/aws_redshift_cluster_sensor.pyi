from airflow.contrib.hooks.redshift_hook import RedshiftHook as RedshiftHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class AwsRedshiftClusterSensor(BaseSensorOperator):
    template_fields: Any
    cluster_identifier: Any
    target_status: Any
    aws_conn_id: Any
    def __init__(self, cluster_identifier, target_status: str = ..., aws_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
