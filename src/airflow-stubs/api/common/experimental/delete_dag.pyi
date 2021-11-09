from airflow import models as models
from airflow.exceptions import DagNotFound as DagNotFound
from airflow.models import DagModel as DagModel, TaskFail as TaskFail
from airflow.models.serialized_dag import SerializedDagModel as SerializedDagModel
from airflow.settings import STORE_SERIALIZED_DAGS as STORE_SERIALIZED_DAGS
from airflow.utils.db import provide_session as provide_session
from typing import Any

log: Any

def delete_dag(dag_id, keep_records_in_log: bool = ..., session: Any | None = ...): ...
