from airflow.exceptions import AirflowException as AirflowException
from airflow.models import DagBag as DagBag, DagModel as DagModel, DagRun as DagRun, TaskInstance as TaskInstance
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.db import provide_session as provide_session
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.state import State as State
from typing import Any

class ExternalTaskSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    allowed_states: Any
    execution_delta: Any
    execution_date_fn: Any
    external_dag_id: Any
    external_task_id: Any
    check_existence: Any
    def __init__(self, external_dag_id, external_task_id: Any | None = ..., allowed_states: Any | None = ..., execution_delta: Any | None = ..., execution_date_fn: Any | None = ..., check_existence: bool = ..., *args, **kwargs) -> None: ...
    def poke(self, context, session: Any | None = ...): ...

class ExternalTaskMarker(DummyOperator):
    template_fields: Any
    ui_color: str
    external_dag_id: Any
    external_task_id: Any
    execution_date: Any
    recursion_depth: Any
    def __init__(self, external_dag_id, external_task_id, execution_date: str = ..., recursion_depth: int = ..., *args, **kwargs) -> None: ...
