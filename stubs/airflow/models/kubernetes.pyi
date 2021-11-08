from airflow.models.base import Base as Base
from airflow.utils.db import provide_session as provide_session
from typing import Any

class KubeResourceVersion(Base):
    __tablename__: str
    one_row_id: Any
    resource_version: Any
    @staticmethod
    def get_current_resource_version(session: Any | None = ...): ...
    @staticmethod
    def checkpoint_resource_version(resource_version, session: Any | None = ...) -> None: ...
    @staticmethod
    def reset_resource_version(session: Any | None = ...): ...

class KubeWorkerIdentifier(Base):
    __tablename__: str
    one_row_id: Any
    worker_uuid: Any
    @staticmethod
    def get_or_create_current_kube_worker_uuid(session: Any | None = ...): ...
    @staticmethod
    def checkpoint_kube_worker_uuid(worker_uuid, session: Any | None = ...) -> None: ...
