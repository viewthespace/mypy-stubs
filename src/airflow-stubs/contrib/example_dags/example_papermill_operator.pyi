from airflow.models import DAG as DAG
from airflow.operators.papermill_operator import PapermillOperator as PapermillOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any
run_this: Any
