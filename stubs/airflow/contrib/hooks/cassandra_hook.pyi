from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

class CassandraHook(BaseHook, LoggingMixin):
    cluster: Any
    keyspace: Any
    session: Any
    def __init__(self, cassandra_conn_id: str = ...) -> None: ...
    def get_conn(self): ...
    def get_cluster(self): ...
    def shutdown_cluster(self) -> None: ...
    @staticmethod
    def get_lb_policy(policy_name, policy_args): ...
    def table_exists(self, table): ...
    def record_exists(self, table, keys): ...
