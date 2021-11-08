from airflow import DAG as DAG
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any
dag: Any
t1: Any
t2: Any
templated_command: str
t3: Any
