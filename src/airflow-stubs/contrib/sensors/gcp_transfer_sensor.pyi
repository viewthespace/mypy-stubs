from airflow.contrib.hooks.gcp_transfer_hook import GCPTransferServiceHook as GCPTransferServiceHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GCPTransferServiceWaitForJobStatusSensor(BaseSensorOperator):
    template_fields: Any
    job_name: Any
    expected_statuses: Any
    project_id: Any
    gcp_cloud_conn_id: Any
    def __init__(self, job_name, expected_statuses, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
