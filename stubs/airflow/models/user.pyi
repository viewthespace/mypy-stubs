from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from typing import Any

class User(Base):
    __tablename__: str
    id: Any
    username: Any
    email: Any
    superuser: Any
    def get_id(self): ...
    def is_superuser(self): ...
