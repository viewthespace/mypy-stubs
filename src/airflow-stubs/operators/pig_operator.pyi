from airflow.hooks.pig_hook import PigCliHook as PigCliHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class PigOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    pigparams_jinja_translate: Any
    pig: Any
    pig_cli_conn_id: Any
    pig_opts: Any
    def __init__(self, pig, pig_cli_conn_id: str = ..., pigparams_jinja_translate: bool = ..., pig_opts: Any | None = ..., *args, **kwargs) -> None: ...
    def get_hook(self): ...
    def prepare_template(self) -> None: ...
    hook: Any
    def execute(self, context) -> None: ...
    def on_kill(self) -> None: ...
