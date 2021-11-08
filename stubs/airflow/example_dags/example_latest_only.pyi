from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.operators.latest_only_operator import LatestOnlyOperator as LatestOnlyOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

dag: Any
latest_only: Any
task1: Any
