from typing import Any

revision: str
down_revision: str
branch_labels: Any
depends_on: Any
connectionhelper: Any

def upgrade() -> None: ...
def downgrade() -> None: ...
