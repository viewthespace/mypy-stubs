from airflow.secrets import BaseSecretsBackend as BaseSecretsBackend
from typing import Optional

CONN_ENV_PREFIX: str
VAR_ENV_PREFIX: str

class EnvironmentVariablesBackend(BaseSecretsBackend):
    def get_conn_uri(self, conn_id: str) -> Optional[str]: ...
    def get_variable(self, key: str) -> Optional[str]: ...
