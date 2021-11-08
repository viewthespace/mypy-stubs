from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.executors.base_executor import BaseExecutor as BaseExecutor
from airflow.executors.local_executor import LocalExecutor as LocalExecutor
from airflow.executors.sequential_executor import SequentialExecutor as SequentialExecutor
from typing import Any

DEFAULT_EXECUTOR: Any
log: Any

def get_default_executor(): ...

class Executors:
    LocalExecutor: str
    SequentialExecutor: str
    CeleryExecutor: str
    DaskExecutor: str
    MesosExecutor: str
    KubernetesExecutor: str
    DebugExecutor: str
