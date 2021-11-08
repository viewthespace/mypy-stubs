from airflow.models import DAG as DAG
from airflow.operators.python_operator import PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

args: Any
affinity: Any
tolerations: Any

def print_stuff() -> None: ...
def use_zip_binary() -> None: ...

start_task: Any
one_task: Any
two_task: Any
three_task: Any
four_task: Any
