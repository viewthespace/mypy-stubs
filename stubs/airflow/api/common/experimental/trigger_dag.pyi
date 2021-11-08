from airflow.exceptions import DagNotFound as DagNotFound, DagRunAlreadyExists as DagRunAlreadyExists
from airflow.models import DagBag as DagBag, DagModel as DagModel, DagRun as DagRun
from airflow.utils import timezone as timezone
from airflow.utils.state import State as State
from datetime import datetime
from typing import Optional, Union

def trigger_dag(dag_id: str, run_id: Optional[str] = ..., conf: Optional[Union[dict, str]] = ..., execution_date: Optional[datetime] = ..., replace_microseconds: bool = ...): ...
