from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from typing import Any

log: Any

class InvalidFernetToken(Exception): ...

class NullFernet:
    is_encrypted: bool
    def decrypt(self, b): ...
    def encrypt(self, b): ...

def get_fernet(): ...
