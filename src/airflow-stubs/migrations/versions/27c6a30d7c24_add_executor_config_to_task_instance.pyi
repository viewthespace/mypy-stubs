from typing import Any

revision: str
down_revision: str
branch_labels: Any
depends_on: Any
TASK_INSTANCE_TABLE: str
NEW_COLUMN: str

def upgrade() -> None: ...
def downgrade() -> None: ...
