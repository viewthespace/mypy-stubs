from airflow.contrib.hooks.redis_hook import RedisHook as RedisHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class RedisPublishOperator(BaseOperator):
    template_fields: Any
    redis_conn_id: Any
    channel: Any
    message: Any
    def __init__(self, channel, message, redis_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
