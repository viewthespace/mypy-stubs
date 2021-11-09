from airflow.api.common.experimental.trigger_dag import trigger_dag as trigger_dag
from airflow.models import BaseOperator as BaseOperator
from airflow.utils import timezone as timezone
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class DagRunOrder:
    run_id: Any
    payload: Any
    def __init__(self, run_id: Any | None = ..., payload: Any | None = ...) -> None: ...

class TriggerDagRunOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    python_callable: Any
    trigger_dag_id: Any
    execution_date: Any
    def __init__(self, trigger_dag_id, python_callable: Any | None = ..., execution_date: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
