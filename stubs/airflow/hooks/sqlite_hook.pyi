from airflow.hooks.dbapi_hook import DbApiHook as DbApiHook

class SqliteHook(DbApiHook):
    conn_name_attr: str
    default_conn_name: str
    supports_autocommit: bool
    def get_conn(self): ...
