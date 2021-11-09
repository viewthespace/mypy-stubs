from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.operators.python_operator import BranchPythonOperator as BranchPythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

branch_1: Any
join_1: Any
true_1: Any
false_1: Any
branch_2: Any
join_2: Any
true_2: Any
false_2: Any
false_3: Any
