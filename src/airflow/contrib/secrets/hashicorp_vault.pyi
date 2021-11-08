import hvac
from airflow.exceptions import AirflowException as AirflowException
from airflow.secrets import BaseSecretsBackend as BaseSecretsBackend
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any, Optional

class VaultBackend(BaseSecretsBackend, LoggingMixin):
    connections_path: Any
    variables_path: Any
    config_path: Any
    url: Any
    auth_type: Any
    kwargs: Any
    token: Any
    username: Any
    password: Any
    role_id: Any
    kubernetes_role: Any
    kubernetes_jwt_path: Any
    secret_id: Any
    mount_point: Any
    kv_engine_version: Any
    gcp_key_path: Any
    gcp_scopes: Any
    def __init__(self, connections_path: str = ..., variables_path: str = ..., config_path: str = ..., url: Optional[str] = ..., auth_type: str = ..., mount_point: str = ..., kv_engine_version: int = ..., token: Optional[str] = ..., username: Optional[str] = ..., password: Optional[str] = ..., role_id: Optional[str] = ..., kubernetes_role: Optional[str] = ..., kubernetes_jwt_path: str = ..., secret_id: Optional[str] = ..., gcp_key_path: Optional[str] = ..., gcp_scopes: Optional[str] = ..., **kwargs) -> None: ...
    def client(self) -> hvac.Client: ...
    def get_conn_uri(self, conn_id: str) -> Optional[str]: ...
    def get_variable(self, key: str) -> Optional[str]: ...
    def get_config(self, key: str) -> Optional[str]: ...
