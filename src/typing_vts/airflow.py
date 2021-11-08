from airflow.models import DAG, DagRun, TaskInstance
from typing import Any, Dict
from typing_extensions import TypedDict

Context = TypedDict('Context', {
    'dag': DAG,
    'dag_run': DagRun,
    'params': Dict[Any, Any],
    'task_instance': TaskInstance,
    'ti': TaskInstance,
    })
