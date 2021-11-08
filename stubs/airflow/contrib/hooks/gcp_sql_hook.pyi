from airflow import AirflowException as AirflowException, LoggingMixin as LoggingMixin
from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.hooks.mysql_hook import MySqlHook as MySqlHook
from airflow.hooks.postgres_hook import PostgresHook as PostgresHook
from airflow.models import Connection as Connection
from airflow.utils.db import provide_session as provide_session
from typing import Any

UNIX_PATH_MAX: int
TIME_TO_SLEEP_IN_SECONDS: int

class CloudSqlOperationStatus:
    PENDING: str
    RUNNING: str
    DONE: str
    UNKNOWN: str

class CloudSqlHook(GoogleCloudBaseHook):
    api_version: Any
    def __init__(self, api_version, gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def get_instance(self, instance, project_id: Any | None = ...): ...
    def create_instance(self, body, project_id: Any | None = ...) -> None: ...
    def patch_instance(self, body, instance, project_id: Any | None = ...) -> None: ...
    def delete_instance(self, instance, project_id: Any | None = ...) -> None: ...
    def get_database(self, instance, database, project_id: Any | None = ...): ...
    def create_database(self, instance, body, project_id: Any | None = ...) -> None: ...
    def patch_database(self, instance, database, body, project_id: Any | None = ...) -> None: ...
    def delete_database(self, instance, database, project_id: Any | None = ...) -> None: ...
    def export_instance(self, instance, body, project_id: Any | None = ...) -> None: ...
    def import_instance(self, instance, body, project_id: Any | None = ...) -> None: ...

CLOUD_SQL_PROXY_DOWNLOAD_URL: str
CLOUD_SQL_PROXY_VERSION_DOWNLOAD_URL: str
GCP_CREDENTIALS_KEY_PATH: str
GCP_CREDENTIALS_KEYFILE_DICT: str

class CloudSqlProxyRunner(LoggingMixin):
    path_prefix: Any
    sql_proxy_was_downloaded: bool
    sql_proxy_version: Any
    download_sql_proxy_dir: Any
    sql_proxy_process: Any
    instance_specification: Any
    project_id: Any
    gcp_conn_id: Any
    command_line_parameters: Any
    cloud_sql_proxy_socket_directory: Any
    sql_proxy_path: Any
    credentials_path: Any
    def __init__(self, path_prefix, instance_specification, gcp_conn_id: str = ..., project_id: Any | None = ..., sql_proxy_version: Any | None = ..., sql_proxy_binary_path: Any | None = ...) -> None: ...
    def start_proxy(self) -> None: ...
    def stop_proxy(self) -> None: ...
    def get_proxy_version(self): ...
    def get_socket_path(self): ...

CONNECTION_URIS: Any
CLOUD_SQL_VALID_DATABASE_TYPES: Any

class CloudSqlDatabaseHook(BaseHook):
    gcp_conn_id: Any
    gcp_cloudsql_conn_id: Any
    cloudsql_connection: Any
    extras: Any
    project_id: Any
    instance: Any
    database: Any
    location: Any
    database_type: Any
    use_proxy: Any
    use_ssl: Any
    sql_proxy_use_tcp: Any
    sql_proxy_version: Any
    sql_proxy_binary_path: Any
    user: Any
    password: Any
    public_ip: Any
    public_port: Any
    sslcert: Any
    sslkey: Any
    sslrootcert: Any
    sql_proxy_tcp_port: Any
    sql_proxy_unique_path: Any
    db_hook: Any
    reserved_tcp_socket: Any
    db_conn_id: Any
    def __init__(self, gcp_cloudsql_conn_id: str = ..., gcp_conn_id: str = ..., default_gcp_project_id: Any | None = ...) -> None: ...
    def validate_ssl_certs(self) -> None: ...
    def validate_socket_path_length(self) -> None: ...
    def create_connection(self, session: Any | None = ...) -> None: ...
    def retrieve_connection(self, session: Any | None = ...): ...
    def delete_connection(self, session: Any | None = ...) -> None: ...
    def get_sqlproxy_runner(self): ...
    def get_database_hook(self): ...
    def cleanup_database_hook(self) -> None: ...
    def reserve_free_tcp_port(self) -> None: ...
    def free_reserved_port(self) -> None: ...
