import typing as T

from .client import Client

default_client: Client


def configure(**options: T.Any) -> None: ...


def notify(exception: BaseException, **options: T.Any) -> None: ...
