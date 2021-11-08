from airflow import DAG as DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator as TriggerDagRunOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

pp: Any

def conditionally_trigger(context, dag_run_obj): ...

dag: Any
trigger: Any
