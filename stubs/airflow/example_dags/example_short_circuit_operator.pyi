from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.operators.python_operator import ShortCircuitOperator as ShortCircuitOperator
from typing import Any

args: Any
dag: Any
cond_true: Any
cond_false: Any
ds_true: Any
ds_false: Any
