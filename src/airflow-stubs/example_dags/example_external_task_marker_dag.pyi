from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.sensors.external_task_sensor import ExternalTaskMarker as ExternalTaskMarker, ExternalTaskSensor as ExternalTaskSensor
from typing import Any

start_date: Any
parent_task: Any
child_task1: Any
child_task2: Any
