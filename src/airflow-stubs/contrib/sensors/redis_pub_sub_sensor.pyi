from airflow.contrib.hooks.redis_hook import RedisHook as RedisHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class RedisPubSubSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    channels: Any
    redis_conn_id: Any
    pubsub: Any
    def __init__(self, channels, redis_conn_id, *args, **kwargs) -> None: ...
    def poke(self, context): ...
