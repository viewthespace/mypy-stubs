from airflow.contrib.hooks.gcp_vision_hook import CloudVisionHook as CloudVisionHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class CloudVisionProductSetCreateOperator(BaseOperator):
    template_fields: Any
    location: Any
    project_id: Any
    product_set: Any
    product_set_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, product_set, location, project_id: Any | None = ..., product_set_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionProductSetGetOperator(BaseOperator):
    template_fields: Any
    location: Any
    project_id: Any
    product_set_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, location, product_set_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionProductSetUpdateOperator(BaseOperator):
    template_fields: Any
    product_set: Any
    update_mask: Any
    location: Any
    project_id: Any
    product_set_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, product_set, location: Any | None = ..., product_set_id: Any | None = ..., project_id: Any | None = ..., update_mask: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionProductSetDeleteOperator(BaseOperator):
    template_fields: Any
    location: Any
    project_id: Any
    product_set_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, location, product_set_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudVisionProductCreateOperator(BaseOperator):
    template_fields: Any
    location: Any
    product: Any
    project_id: Any
    product_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, location, product, project_id: Any | None = ..., product_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionProductGetOperator(BaseOperator):
    template_fields: Any
    location: Any
    product_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, location, product_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionProductUpdateOperator(BaseOperator):
    template_fields: Any
    product: Any
    location: Any
    product_id: Any
    project_id: Any
    update_mask: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, product, location: Any | None = ..., product_id: Any | None = ..., project_id: Any | None = ..., update_mask: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionProductDeleteOperator(BaseOperator):
    template_fields: Any
    location: Any
    product_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, location, product_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudVisionAnnotateImageOperator(BaseOperator):
    template_fields: Any
    request: Any
    retry: Any
    timeout: Any
    gcp_conn_id: Any
    def __init__(self, request, retry: Any | None = ..., timeout: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionReferenceImageCreateOperator(BaseOperator):
    template_fields: Any
    location: Any
    product_id: Any
    reference_image: Any
    reference_image_id: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, location, reference_image, product_id, reference_image_id: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionAddProductToProductSetOperator(BaseOperator):
    template_fields: Any
    product_set_id: Any
    product_id: Any
    location: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, product_set_id, product_id, location, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionRemoveProductFromProductSetOperator(BaseOperator):
    template_fields: Any
    product_set_id: Any
    product_id: Any
    location: Any
    project_id: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, product_set_id, product_id, location, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionDetectTextOperator(BaseOperator):
    template_fields: Any
    image: Any
    max_results: Any
    retry: Any
    timeout: Any
    gcp_conn_id: Any
    kwargs: Any
    additional_properties: Any
    def __init__(self, image, max_results: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., language_hints: Any | None = ..., web_detection_params: Any | None = ..., additional_properties: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionDetectDocumentTextOperator(BaseOperator):
    template_fields: Any
    image: Any
    max_results: Any
    retry: Any
    timeout: Any
    gcp_conn_id: Any
    additional_properties: Any
    def __init__(self, image, max_results: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., language_hints: Any | None = ..., web_detection_params: Any | None = ..., additional_properties: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionDetectImageLabelsOperator(BaseOperator):
    template_fields: Any
    image: Any
    max_results: Any
    retry: Any
    timeout: Any
    gcp_conn_id: Any
    additional_properties: Any
    def __init__(self, image, max_results: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., additional_properties: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVisionDetectImageSafeSearchOperator(BaseOperator):
    template_fields: Any
    image: Any
    max_results: Any
    retry: Any
    timeout: Any
    gcp_conn_id: Any
    additional_properties: Any
    def __init__(self, image, max_results: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., additional_properties: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

def prepare_additional_parameters(additional_properties, language_hints, web_detection_params): ...
