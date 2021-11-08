from typing import Any

revision: str
down_revision: str
branch_labels: Any
depends_on: Any
RESOURCE_TABLE: str

def upgrade() -> None: ...
def downgrade() -> None: ...
