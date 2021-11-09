from airflow.exceptions import AirflowException as AirflowException
from typing import Any, Dict, Optional, Sequence

log: Any
AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT: str

def get_credentials_and_project_id(key_path: Optional[str] = ..., keyfile_dict: Optional[Dict[str, str]] = ..., scopes: Optional[Sequence[str]] = ..., delegate_to: Optional[str] = ...): ...
