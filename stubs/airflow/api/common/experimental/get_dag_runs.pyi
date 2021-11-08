from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag
from airflow.models import DagRun as DagRun
from typing import Any, Dict, List, Optional

def get_dag_runs(dag_id: str, state: Optional[str] = ..., run_url_route: str = ...) -> List[Dict[str, Any]]: ...
