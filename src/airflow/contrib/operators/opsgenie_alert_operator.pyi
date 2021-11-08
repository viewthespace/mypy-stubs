from airflow.contrib.hooks.opsgenie_alert_hook import OpsgenieAlertHook as OpsgenieAlertHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class OpsgenieAlertOperator(BaseOperator):
    template_fields: Any
    message: Any
    opsgenie_conn_id: Any
    alias: Any
    description: Any
    responders: Any
    visibleTo: Any
    actions: Any
    tags: Any
    details: Any
    entity: Any
    source: Any
    priority: Any
    user: Any
    note: Any
    hook: Any
    def __init__(self, message, opsgenie_conn_id: str = ..., alias: Any | None = ..., description: Any | None = ..., responders: Any | None = ..., visibleTo: Any | None = ..., actions: Any | None = ..., tags: Any | None = ..., details: Any | None = ..., entity: Any | None = ..., source: Any | None = ..., priority: Any | None = ..., user: Any | None = ..., note: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
