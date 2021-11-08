from typing import Any

revision: str
down_revision: str
branch_labels: Any
depends_on: Any
TABLE_NAME: str

def upgrade() -> None: ...
def downgrade() -> None: ...
