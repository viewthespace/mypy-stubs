from airflow import DAG as DAG
from airflow.contrib.operators.databricks_operator import DatabricksSubmitRunOperator as DatabricksSubmitRunOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any
new_cluster: Any
notebook_task_params: Any
notebook_task: Any
spark_jar_task: Any
