from airflow.hooks.dbapi_hook import DbApiHook as DbApiHook
from typing import Any

class SnowflakeHook(DbApiHook):
    conn_name_attr: str
    default_conn_name: str
    supports_autocommit: bool
    account: Any
    warehouse: Any
    database: Any
    region: Any
    role: Any
    schema: Any
    authenticator: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def get_uri(self): ...
    def get_conn(self): ...
    def set_autocommit(self, conn, autocommit) -> None: ...
