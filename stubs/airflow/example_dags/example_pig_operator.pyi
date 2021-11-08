from airflow.models import DAG as DAG
from airflow.operators.pig_operator import PigOperator as PigOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

args: Any
dag: Any
run_this: Any
