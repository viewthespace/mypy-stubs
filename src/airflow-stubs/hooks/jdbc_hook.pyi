from airflow.hooks.dbapi_hook import DbApiHook as DbApiHook

class JdbcHook(DbApiHook):
    conn_name_attr: str
    default_conn_name: str
    supports_autocommit: bool
    def get_conn(self): ...
    def set_autocommit(self, conn, autocommit) -> None: ...
    def get_autocommit(self, conn): ...
