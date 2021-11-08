from airflow import DAG as DAG
from airflow.contrib.operators.qubole_operator import QuboleOperator as QuboleOperator
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.operators.python_operator import BranchPythonOperator as BranchPythonOperator, PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any

def compare_result(**kwargs): ...

t1: Any
t2: Any
t3: Any
options: Any
branching: Any
join: Any
t4: Any
t5: Any
t6: Any
t7: Any
t8: Any
t9: Any
t10: Any
prog: str
t11: Any
