from airflow import version as version
from airflow.contrib.utils.gcp_credentials_provider import get_credentials_and_project_id as get_credentials_and_project_id
from airflow.exceptions import AirflowException as AirflowException
from airflow.secrets import BaseSecretsBackend as BaseSecretsBackend
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from google.cloud.secretmanager_v1 import SecretManagerServiceClient
from typing import Any, Optional

SECRET_ID_PATTERN: str

class CloudSecretsManagerBackend(BaseSecretsBackend, LoggingMixin):
    connections_prefix: Any
    variables_prefix: Any
    gcp_key_path: Any
    gcp_scopes: Any
    sep: Any
    credentials: Any
    project_id: Any
    def __init__(self, connections_prefix: str = ..., variables_prefix: str = ..., gcp_key_path: Optional[str] = ..., gcp_scopes: Optional[str] = ..., sep: str = ..., **kwargs) -> None: ...
    def client(self) -> SecretManagerServiceClient: ...
    def get_conn_uri(self, conn_id): ...
    def get_variable(self, key: str) -> Optional[str]: ...
