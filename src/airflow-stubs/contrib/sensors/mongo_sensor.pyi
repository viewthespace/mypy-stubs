from airflow.contrib.hooks.mongo_hook import MongoHook as MongoHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class MongoSensor(BaseSensorOperator):
    template_fields: Any
    mongo_conn_id: Any
    collection: Any
    query: Any
    def __init__(self, collection, query, mongo_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
