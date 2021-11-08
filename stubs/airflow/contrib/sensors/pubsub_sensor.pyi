from airflow.contrib.hooks.gcp_pubsub_hook import PubSubHook as PubSubHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class PubSubPullSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    gcp_conn_id: Any
    delegate_to: Any
    project: Any
    subscription: Any
    max_messages: Any
    return_immediately: Any
    ack_messages: Any
    def __init__(self, project, subscription, max_messages: int = ..., return_immediately: bool = ..., ack_messages: bool = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
    def poke(self, context): ...
