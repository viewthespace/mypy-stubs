from airflow.contrib.hooks.gcp_pubsub_hook import PubSubHook as PubSubHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class PubSubTopicCreateOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    project: Any
    topic: Any
    fail_if_exists: Any
    gcp_conn_id: Any
    delegate_to: Any
    def __init__(self, project, topic, fail_if_exists: bool = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class PubSubSubscriptionCreateOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    topic_project: Any
    topic: Any
    subscription: Any
    subscription_project: Any
    ack_deadline_secs: Any
    fail_if_exists: Any
    gcp_conn_id: Any
    delegate_to: Any
    def __init__(self, topic_project, topic, subscription: Any | None = ..., subscription_project: Any | None = ..., ack_deadline_secs: int = ..., fail_if_exists: bool = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class PubSubTopicDeleteOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    project: Any
    topic: Any
    fail_if_not_exists: Any
    gcp_conn_id: Any
    delegate_to: Any
    def __init__(self, project, topic, fail_if_not_exists: bool = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class PubSubSubscriptionDeleteOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    project: Any
    subscription: Any
    fail_if_not_exists: Any
    gcp_conn_id: Any
    delegate_to: Any
    def __init__(self, project, subscription, fail_if_not_exists: bool = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class PubSubPublishOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    gcp_conn_id: Any
    delegate_to: Any
    project: Any
    topic: Any
    messages: Any
    def __init__(self, project, topic, messages, gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
