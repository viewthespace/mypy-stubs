from airflow.hooks.dbapi_hook import DbApiHook as DbApiHook
from typing import Any

class OracleHook(DbApiHook):
    conn_name_attr: str
    default_conn_name: str
    supports_autocommit: bool
    def get_conn(self): ...
    def insert_rows(self, table, rows, target_fields: Any | None = ..., commit_every: int = ...) -> None: ...
    def bulk_insert_rows(self, table, rows, target_fields: Any | None = ..., commit_every: int = ...) -> None: ...
