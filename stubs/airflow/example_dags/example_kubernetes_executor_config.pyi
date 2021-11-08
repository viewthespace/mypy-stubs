from airflow.contrib.example_dags.libs.helper import print_stuff as print_stuff
from airflow.models import DAG as DAG
from airflow.operators.python_operator import PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any

def test_volume_mount() -> None: ...

start_task: Any
second_task: Any
third_task: Any
other_ns_task: Any
