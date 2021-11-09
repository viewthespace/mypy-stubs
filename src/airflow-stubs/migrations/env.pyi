from airflow import models as models, settings as settings
from typing import Any

config: Any
target_metadata: Any
COMPARE_TYPE: bool

def run_migrations_offline() -> None: ...
def run_migrations_online() -> None: ...
