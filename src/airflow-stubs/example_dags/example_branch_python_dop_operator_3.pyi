from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.operators.python_operator import BranchPythonOperator as BranchPythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

args: Any
dag: Any

def should_run(**kwargs): ...

cond: Any
dummy_task_1: Any
dummy_task_2: Any
