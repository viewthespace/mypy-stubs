from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils import timezone as timezone
from airflow.utils.db import provide_session as provide_session

class RunnableExecDateDep(BaseTIDep):
    NAME: str
    IGNOREABLE: bool
