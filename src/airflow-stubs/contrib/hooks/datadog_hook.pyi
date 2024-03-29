from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

class DatadogHook(BaseHook, LoggingMixin):
    api_key: Any
    app_key: Any
    source_type_name: Any
    host: Any
    def __init__(self, datadog_conn_id: str = ...) -> None: ...
    def validate_response(self, response) -> None: ...
    def send_metric(self, metric_name, datapoint, tags: Any | None = ..., type_: Any | None = ..., interval: Any | None = ...): ...
    def query_metric(self, query, from_seconds_ago, to_seconds_ago): ...
    def post_event(self, title, text, aggregation_key: Any | None = ..., alert_type: Any | None = ..., date_happened: Any | None = ..., handle: Any | None = ..., priority: Any | None = ..., related_event_id: Any | None = ..., tags: Any | None = ..., device_name: Any | None = ...): ...
