from airflow.models import DAG as DAG
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

args: Any
dag: Any
run_this_last: Any
run_this: Any
task: Any
also_run_this: Any
