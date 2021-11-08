from airflow import models as models
from airflow.contrib.operators.dataproc_operator import DataProcPigOperator as DataProcPigOperator, DataprocClusterCreateOperator as DataprocClusterCreateOperator, DataprocClusterDeleteOperator as DataprocClusterDeleteOperator
from typing import Any

default_args: Any
CLUSTER_NAME: Any
PROJECT_ID: Any
REGION: Any
create_task: Any
pig_task: Any
delete_task: Any
