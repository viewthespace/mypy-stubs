from airflow.contrib.hooks.gcp_dlp_hook import CloudDLPHook as CloudDLPHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class CloudDLPCancelDLPJobOperator(BaseOperator):
    template_fields: Any
    dlp_job_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, dlp_job_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudDLPCreateDeidentifyTemplateOperator(BaseOperator):
    template_fields: Any
    organization_id: Any
    project_id: Any
    deidentify_template: Any
    template_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, organization_id: Any | None = ..., project_id: Any | None = ..., deidentify_template: Any | None = ..., template_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPCreateDLPJobOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    inspect_job: Any
    risk_job: Any
    job_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    wait_until_finished: Any
    gcp_conn_id: Any
    def __init__(self, project_id: Any | None = ..., inspect_job: Any | None = ..., risk_job: Any | None = ..., job_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., wait_until_finished: bool = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPCreateInspectTemplateOperator(BaseOperator):
    template_fields: Any
    organization_id: Any
    project_id: Any
    inspect_template: Any
    template_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, organization_id: Any | None = ..., project_id: Any | None = ..., inspect_template: Any | None = ..., template_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPCreateJobTriggerOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    job_trigger: Any
    trigger_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, project_id: Any | None = ..., job_trigger: Any | None = ..., trigger_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPCreateStoredInfoTypeOperator(BaseOperator):
    template_fields: Any
    organization_id: Any
    project_id: Any
    config: Any
    stored_info_type_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, organization_id: Any | None = ..., project_id: Any | None = ..., config: Any | None = ..., stored_info_type_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPDeidentifyContentOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    deidentify_config: Any
    inspect_config: Any
    item: Any
    inspect_template_name: Any
    deidentify_template_name: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, project_id: Any | None = ..., deidentify_config: Any | None = ..., inspect_config: Any | None = ..., item: Any | None = ..., inspect_template_name: Any | None = ..., deidentify_template_name: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPDeleteDeidentifyTemplateOperator(BaseOperator):
    template_fields: Any
    template_id: Any
    organization_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, template_id, organization_id: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudDLPDeleteDlpJobOperator(BaseOperator):
    template_fields: Any
    dlp_job_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, dlp_job_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudDLPDeleteInspectTemplateOperator(BaseOperator):
    template_fields: Any
    template_id: Any
    organization_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, template_id, organization_id: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudDLPDeleteJobTriggerOperator(BaseOperator):
    template_fields: Any
    job_trigger_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, job_trigger_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudDLPDeleteStoredInfoTypeOperator(BaseOperator):
    template_fields: Any
    stored_info_type_id: Any
    organization_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, stored_info_type_id, organization_id: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudDLPGetDeidentifyTemplateOperator(BaseOperator):
    template_fields: Any
    template_id: Any
    organization_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, template_id, organization_id: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPGetDlpJobOperator(BaseOperator):
    template_fields: Any
    dlp_job_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, dlp_job_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPGetInspectTemplateOperator(BaseOperator):
    template_fields: Any
    template_id: Any
    organization_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, template_id, organization_id: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPGetJobTripperOperator(BaseOperator):
    template_fields: Any
    job_trigger_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, job_trigger_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPGetStoredInfoTypeOperator(BaseOperator):
    template_fields: Any
    stored_info_type_id: Any
    organization_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, stored_info_type_id, organization_id: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPInspectContentOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    inspect_config: Any
    item: Any
    inspect_template_name: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, project_id: Any | None = ..., inspect_config: Any | None = ..., item: Any | None = ..., inspect_template_name: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPListDeidentifyTemplatesOperator(BaseOperator):
    template_fields: Any
    organization_id: Any
    project_id: Any
    page_size: Any
    order_by: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, organization_id: Any | None = ..., project_id: Any | None = ..., page_size: Any | None = ..., order_by: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPListDlpJobsOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    results_filter: Any
    page_size: Any
    job_type: Any
    order_by: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, project_id: Any | None = ..., results_filter: Any | None = ..., page_size: Any | None = ..., job_type: Any | None = ..., order_by: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPListInfoTypesOperator(BaseOperator):
    template_fields: Any
    language_code: Any
    results_filter: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, language_code: Any | None = ..., results_filter: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPListInspectTemplatesOperator(BaseOperator):
    template_fields: Any
    organization_id: Any
    project_id: Any
    page_size: Any
    order_by: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, organization_id: Any | None = ..., project_id: Any | None = ..., page_size: Any | None = ..., order_by: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPListJobTriggersOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    page_size: Any
    order_by: Any
    results_filter: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, project_id: Any | None = ..., page_size: Any | None = ..., order_by: Any | None = ..., results_filter: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPListStoredInfoTypesOperator(BaseOperator):
    template_fields: Any
    organization_id: Any
    project_id: Any
    page_size: Any
    order_by: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, organization_id: Any | None = ..., project_id: Any | None = ..., page_size: Any | None = ..., order_by: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPRedactImageOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    inspect_config: Any
    image_redaction_configs: Any
    include_findings: Any
    byte_item: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, project_id: Any | None = ..., inspect_config: Any | None = ..., image_redaction_configs: Any | None = ..., include_findings: Any | None = ..., byte_item: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPReidentifyContentOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    reidentify_config: Any
    inspect_config: Any
    item: Any
    inspect_template_name: Any
    reidentify_template_name: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, project_id: Any | None = ..., reidentify_config: Any | None = ..., inspect_config: Any | None = ..., item: Any | None = ..., inspect_template_name: Any | None = ..., reidentify_template_name: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPUpdateDeidentifyTemplateOperator(BaseOperator):
    template_fields: Any
    template_id: Any
    organization_id: Any
    project_id: Any
    deidentify_template: Any
    update_mask: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, template_id, organization_id: Any | None = ..., project_id: Any | None = ..., deidentify_template: Any | None = ..., update_mask: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPUpdateInspectTemplateOperator(BaseOperator):
    template_fields: Any
    template_id: Any
    organization_id: Any
    project_id: Any
    inspect_template: Any
    update_mask: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, template_id, organization_id: Any | None = ..., project_id: Any | None = ..., inspect_template: Any | None = ..., update_mask: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPUpdateJobTriggerOperator(BaseOperator):
    template_fields: Any
    job_trigger_id: Any
    project_id: Any
    job_trigger: Any
    update_mask: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, job_trigger_id, project_id: Any | None = ..., job_trigger: Any | None = ..., update_mask: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudDLPUpdateStoredInfoTypeOperator(BaseOperator):
    template_fields: Any
    stored_info_type_id: Any
    organization_id: Any
    project_id: Any
    config: Any
    update_mask: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, stored_info_type_id, organization_id: Any | None = ..., project_id: Any | None = ..., config: Any | None = ..., update_mask: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
