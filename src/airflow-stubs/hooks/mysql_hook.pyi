from airflow.hooks.dbapi_hook import DbApiHook as DbApiHook
from typing import Any

class MySqlHook(DbApiHook):
    conn_name_attr: str
    default_conn_name: str
    supports_autocommit: bool
    schema: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def set_autocommit(self, conn, autocommit) -> None: ...
    def get_autocommit(self, conn): ...
    def get_conn(self): ...
    def get_uri(self): ...
    def bulk_load(self, table, tmp_file) -> None: ...
    def bulk_dump(self, table, tmp_file) -> None: ...
    def get_iam_token(self, conn): ...
    def bulk_load_custom(self, table, tmp_file, duplicate_key_handling: str = ..., extra_options: str = ...) -> None: ...
