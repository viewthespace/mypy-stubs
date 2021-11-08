from airflow import settings as settings
from airflow.exceptions import AirflowException as AirflowException
from airflow.executors.sequential_executor import SequentialExecutor as SequentialExecutor
from airflow.models import BaseOperator as BaseOperator, Pool as Pool
from airflow.utils.db import provide_session as provide_session
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SubDagOperator(BaseOperator):
    ui_color: str
    ui_fgcolor: str
    subdag: Any
    executor: Any
    def __init__(self, subdag, executor=..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
