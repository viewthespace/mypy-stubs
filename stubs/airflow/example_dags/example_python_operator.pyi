from airflow.models import DAG as DAG
from airflow.operators.python_operator import PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

args: Any
dag: Any

def print_context(ds, **kwargs): ...

run_this: Any

def my_sleeping_function(random_base) -> None: ...

task: Any
