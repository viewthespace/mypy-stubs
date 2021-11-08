from airflow.configuration import conf as conf
from airflow.exceptions import DagNotFound as DagNotFound, DagRunNotFound as DagRunNotFound, TaskNotFound as TaskNotFound
from airflow.models import DagBag as DagBag, DagModel as DagModel, DagRun as DagRun
from datetime import datetime
from typing import Optional

def check_and_get_dag(dag_id: str, task_id: Optional[str] = ...) -> DagModel: ...
def check_and_get_dagrun(dag: DagModel, execution_date: datetime) -> DagRun: ...
