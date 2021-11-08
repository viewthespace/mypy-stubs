from airflow.contrib.hooks.gcp_mlengine_hook import MLEngineHook as MLEngineHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.operators import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

log: Any

class MLEngineBatchPredictionOperator(BaseOperator):
    template_fields: Any
    def __init__(self, project_id, job_id, region, data_format, input_paths, output_path, model_name: Any | None = ..., version_name: Any | None = ..., uri: Any | None = ..., max_worker_count: Any | None = ..., runtime_version: Any | None = ..., signature_name: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class MLEngineModelOperator(BaseOperator):
    template_fields: Any
    def __init__(self, project_id, model, operation: str = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class MLEngineVersionOperator(BaseOperator):
    template_fields: Any
    def __init__(self, project_id, model_name, version_name: Any | None = ..., version: Any | None = ..., operation: str = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class MLEngineTrainingOperator(BaseOperator):
    template_fields: Any
    def __init__(self, project_id, job_id, package_uris, training_python_module, training_args, region, scale_tier: Any | None = ..., master_type: Any | None = ..., runtime_version: Any | None = ..., python_version: Any | None = ..., job_dir: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., mode: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
