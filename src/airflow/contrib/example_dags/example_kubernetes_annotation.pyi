from airflow.models import DAG as DAG
from airflow.operators.python_operator import PythonOperator as PythonOperator
from typing import Any

args: Any
dag: Any

def print_stuff() -> None: ...

start_task: Any
