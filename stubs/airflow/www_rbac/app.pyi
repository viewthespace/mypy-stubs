from airflow import settings as settings, version as version
from airflow.configuration import conf as conf
from airflow.logging_config import configure_logging as configure_logging
from airflow.settings import STATE_COLORS as STATE_COLORS
from airflow.www_rbac.static_config import configure_manifest_files as configure_manifest_files
from typing import Any

app: Any
appbuilder: Any
csrf: Any
log: Any

def create_app(config: Any | None = ..., session: Any | None = ..., testing: bool = ..., app_name: str = ...): ...
def root_app(env, resp): ...
def cached_app(config: Any | None = ..., session: Any | None = ..., testing: bool = ...): ...
def cached_appbuilder(config: Any | None = ..., testing: bool = ...): ...
