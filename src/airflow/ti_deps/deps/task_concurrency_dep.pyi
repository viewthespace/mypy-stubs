from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.db import provide_session as provide_session

class TaskConcurrencyDep(BaseTIDep):
    NAME: str
    IGNOREABLE: bool
    IS_TASK_DEP: bool
