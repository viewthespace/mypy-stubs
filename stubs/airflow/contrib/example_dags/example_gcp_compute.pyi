from airflow import models as models
from airflow.contrib.operators.gcp_compute_operator import GceInstanceStartOperator as GceInstanceStartOperator, GceInstanceStopOperator as GceInstanceStopOperator, GceSetMachineTypeOperator as GceSetMachineTypeOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

GCP_PROJECT_ID: Any
GCE_ZONE: Any
GCE_INSTANCE: Any
default_args: Any
GCE_SHORT_MACHINE_TYPE_NAME: Any
SET_MACHINE_TYPE_BODY: Any
gce_instance_start: Any
gce_instance_start2: Any
gce_instance_stop: Any
gce_instance_stop2: Any
gce_set_machine_type: Any
gce_set_machine_type2: Any
