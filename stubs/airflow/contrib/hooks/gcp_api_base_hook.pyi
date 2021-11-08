import tenacity
from airflow import version as version
from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

log: Any
INVALID_KEYS: Any
INVALID_REASONS: Any

def is_soft_quota_exception(exception): ...

class retry_if_temporary_quota(tenacity.retry_if_exception):
    def __init__(self) -> None: ...

class GoogleCloudBaseHook(BaseHook):
    gcp_conn_id: Any
    delegate_to: Any
    extras: Any
    def __init__(self, gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    @property
    def project_id(self): ...
    @property
    def num_retries(self): ...
    @staticmethod
    def quota_retry(*args, **kwargs): ...
    @staticmethod
    def catch_http_exception(func): ...
    @staticmethod
    def fallback_to_default_project_id(func): ...
    class _Decorators:
        @staticmethod
        def provide_gcp_credential_file(func): ...
