from airflow.models import DAG as DAG
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.operators.python_operator import PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

pp: Any
dag: Any

def run_this_func(ds, **kwargs) -> None: ...

run_this: Any
bash_task: Any
