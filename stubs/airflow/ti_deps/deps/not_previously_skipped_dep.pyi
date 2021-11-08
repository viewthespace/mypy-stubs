from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep

class NotPreviouslySkippedDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    IS_TASK_DEP: bool
