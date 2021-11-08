from airflow import executors as executors, hooks as hooks, macros as macros, operators as operators, sensors as sensors, settings as settings, utils as utils, version as version
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import DAG as DAG
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from flask_admin import BaseView
from typing import Any

login: Any
log: Any

def load_login() -> None: ...

class AirflowViewPlugin(BaseView): ...

class AirflowMacroPlugin:
    namespace: Any
    def __init__(self, namespace) -> None: ...
