from airflow import DAG as DAG
from airflow.operators.python_operator import PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

args: Any
dag: Any
value_1: Any
value_2: Any

def push(**kwargs) -> None: ...
def push_by_returning(**kwargs): ...
def puller(**kwargs) -> None: ...

push1: Any
push2: Any
pull: Any
