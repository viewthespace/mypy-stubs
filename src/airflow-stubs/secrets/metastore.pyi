from airflow.secrets import BaseSecretsBackend as BaseSecretsBackend
from airflow.utils.db import provide_session as provide_session
from typing import Any

class MetastoreBackend(BaseSecretsBackend):
    def get_connections(self, conn_id, session: Any | None = ...): ...
    def get_variable(self, key, session: Any | None = ...): ...
