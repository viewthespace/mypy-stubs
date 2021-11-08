from airflow import jobs as jobs, models as models, settings as settings, version as version
from airflow.configuration import conf as conf
from airflow.logging_config import configure_logging as configure_logging
from airflow.models.connection import Connection as Connection
from airflow.settings import STATE_COLORS as STATE_COLORS, Session as Session
from airflow.utils.net import get_hostname as get_hostname
from airflow.www.blueprints import routes as routes
from typing import Any

csrf: Any
log: Any

def create_app(config: Any | None = ..., testing: bool = ...): ...

app: Any

def root_app(env, resp): ...
def cached_app(config: Any | None = ..., testing: bool = ...): ...
