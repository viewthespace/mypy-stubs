from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_compute_hook import GceHook as GceHook
from airflow.contrib.utils.gcp_field_sanitizer import GcpBodyFieldSanitizer as GcpBodyFieldSanitizer
from airflow.contrib.utils.gcp_field_validator import GcpBodyFieldValidator as GcpBodyFieldValidator
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GceBaseOperator(BaseOperator):
    project_id: Any
    zone: Any
    resource_id: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, zone, resource_id, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class GceInstanceStartOperator(GceBaseOperator):
    template_fields: Any
    def __init__(self, zone, resource_id, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class GceInstanceStopOperator(GceBaseOperator):
    template_fields: Any
    def __init__(self, zone, resource_id, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

SET_MACHINE_TYPE_VALIDATION_SPECIFICATION: Any

class GceSetMachineTypeOperator(GceBaseOperator):
    template_fields: Any
    body: Any
    def __init__(self, zone, resource_id, body, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., validate_body: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

GCE_INSTANCE_TEMPLATE_VALIDATION_PATCH_SPECIFICATION: Any
GCE_INSTANCE_TEMPLATE_FIELDS_TO_SANITIZE: Any

class GceInstanceTemplateCopyOperator(GceBaseOperator):
    template_fields: Any
    body_patch: Any
    request_id: Any
    def __init__(self, resource_id, body_patch, project_id: Any | None = ..., request_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., validate_body: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class GceInstanceGroupManagerUpdateTemplateOperator(GceBaseOperator):
    template_fields: Any
    zone: Any
    source_template: Any
    destination_template: Any
    request_id: Any
    update_policy: Any
    def __init__(self, resource_id, zone, source_template, destination_template, project_id: Any | None = ..., update_policy: Any | None = ..., request_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
