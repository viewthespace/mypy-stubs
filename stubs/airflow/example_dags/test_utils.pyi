from airflow.models import DAG as DAG
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

dag: Any
task: Any
