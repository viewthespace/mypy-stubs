from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.db import provide_session as provide_session
from airflow.utils.state import State as State
from typing import Any

STATES_TO_COUNT_AS_RUNNING: Any

class PoolSlotsAvailableDep(BaseTIDep):
    NAME: str
    IGNOREABLE: bool
