from airflow import models as models
from airflow.contrib.operators.dataproc_operator import DataprocClusterCreateOperator as DataprocClusterCreateOperator, DataprocClusterDeleteOperator as DataprocClusterDeleteOperator
from typing import Any

PROJECT_ID: Any
CLUSTER_NAME: Any
REGION: Any
ZONE: Any
create_cluster: Any
delete_cluster: Any
