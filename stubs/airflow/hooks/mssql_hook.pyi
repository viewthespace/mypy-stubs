from airflow.hooks.dbapi_hook import DbApiHook as DbApiHook
from typing import Any

class MsSqlHook(DbApiHook):
    conn_name_attr: str
    default_conn_name: str
    supports_autocommit: bool
    schema: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def get_conn(self): ...
    def set_autocommit(self, conn, autocommit) -> None: ...
    def get_autocommit(self, conn): ...
