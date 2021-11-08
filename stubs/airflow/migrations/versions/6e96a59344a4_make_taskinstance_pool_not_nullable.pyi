from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

revision: str
down_revision: str
branch_labels: Any
depends_on: Any
Base: Any
ID_LEN: int

class TaskInstance(Base):
    __tablename__: str
    task_id: Any
    dag_id: Any
    execution_date: Any
    start_date: Any
    end_date: Any
    duration: Any
    state: Any
    max_tries: Any
    hostname: Any
    unixname: Any
    job_id: Any
    pool: Any
    queue: Any
    priority_weight: Any
    operator: Any
    queued_dttm: Any
    pid: Any
    executor_config: Any

def upgrade() -> None: ...
def downgrade() -> None: ...
