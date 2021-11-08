from airflow.configuration import conf as conf
from airflow.utils.db import provide_session as provide_session
from airflow.utils.state import State as State
from blinker import signal as signal
from typing import Any

log: Any

class DummySentry:
    @classmethod
    def add_tagging(cls, task_instance) -> None: ...
    @classmethod
    def add_breadcrumbs(cls, task_instance, session: Any | None = ...) -> None: ...
    @classmethod
    def enrich_errors(cls, run): ...
    def flush(self) -> None: ...

class ConfiguredSentry(DummySentry):
    SCOPE_TAGS: Any
    SCOPE_CRUMBS: Any
    def __init__(self) -> None: ...
    @classmethod
    def add_tagging(self, task_instance) -> None: ...
    @classmethod
    def add_breadcrumbs(self, task_instance, session: Any | None = ...) -> None: ...
    @classmethod
    def enrich_errors(self, func): ...
    def flush(self) -> None: ...

Sentry: DummySentry
