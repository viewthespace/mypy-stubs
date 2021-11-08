from airflow import DAG as DAG
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.operators.python_operator import PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

dag: Any

def my_py_command(ds, **kwargs): ...

my_templated_command: str
run_this: Any
also_run_this: Any
