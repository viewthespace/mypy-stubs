from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.utils.module_loading import import_string as import_string
from typing import Any

log: Any

def configure_logging(): ...
def validate_logging_config(logging_config): ...
