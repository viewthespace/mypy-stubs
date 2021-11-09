from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator as KubernetesPodOperator
from airflow.models import DAG as DAG
from airflow.utils.dates import days_ago as days_ago
from typing import Any

log: Any
default_args: Any
tolerations: Any
k: Any
