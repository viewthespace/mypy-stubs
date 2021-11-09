from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

log: Any

class SalesforceHook(BaseHook):
    conn_id: Any
    connection: Any
    extras: Any
    def __init__(self, conn_id, *args, **kwargs) -> None: ...
    sf: Any
    def sign_in(self): ...
    def make_query(self, query): ...
    def describe_object(self, obj): ...
    def get_available_fields(self, obj): ...
    def get_object_from_salesforce(self, obj, fields): ...
    def write_object_to_file(self, query_results, filename, fmt: str = ..., coerce_to_timestamp: bool = ..., record_time_added: bool = ...): ...