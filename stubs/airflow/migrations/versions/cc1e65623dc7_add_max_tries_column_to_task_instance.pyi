from airflow import settings as settings
from airflow.models import DagBag as DagBag
from typing import Any

revision: str
down_revision: str
branch_labels: Any
depends_on: Any
Base: Any
BATCH_SIZE: int
ID_LEN: int

class TaskInstance(Base):
    __tablename__: str
    task_id: Any
    dag_id: Any
    execution_date: Any
    max_tries: Any
    try_number: Any

def upgrade() -> None: ...
def downgrade() -> None: ...
