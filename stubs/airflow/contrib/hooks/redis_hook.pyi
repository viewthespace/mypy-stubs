from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class RedisHook(BaseHook):
    redis_conn_id: Any
    redis: Any
    host: Any
    port: Any
    password: Any
    db: Any
    def __init__(self, redis_conn_id: str = ...) -> None: ...
    def get_conn(self): ...
