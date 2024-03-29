from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from typing import Any

class NameDeterminer:
    label: Any
    id_label: Any
    get_path: Any
    def __init__(self, label, id_label, get_path) -> None: ...
    def get_entity_with_name(self, entity, entity_id, location, project_id): ...

class CloudVisionHook(GoogleCloudBaseHook):
    product_name_determiner: Any
    product_set_name_determiner: Any
    def __init__(self, gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def annotator_client(self): ...
    def create_product_set(self, location, product_set, project_id: Any | None = ..., product_set_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    def get_product_set(self, location, product_set_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    def update_product_set(self, product_set, location: Any | None = ..., product_set_id: Any | None = ..., update_mask: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    def delete_product_set(self, location, product_set_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...) -> None: ...
    def create_product(self, location, product, project_id: Any | None = ..., product_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    def get_product(self, location, product_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    def update_product(self, product, location: Any | None = ..., product_id: Any | None = ..., update_mask: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    def delete_product(self, location, product_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...) -> None: ...
    def create_reference_image(self, location, product_id, reference_image, reference_image_id: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    def delete_reference_image(self, location, product_id, reference_image_id, project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    def add_product_to_product_set(self, product_set_id, product_id, location: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...) -> None: ...
    def remove_product_from_product_set(self, product_set_id, product_id, location: Any | None = ..., project_id: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...) -> None: ...
    def annotate_image(self, request, retry: Any | None = ..., timeout: Any | None = ...): ...
    def batch_annotate_images(self, requests, retry: Any | None = ..., timeout: Any | None = ...): ...
    def text_detection(self, image, max_results: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., additional_properties: Any | None = ...): ...
    def document_text_detection(self, image, max_results: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., additional_properties: Any | None = ...): ...
    def label_detection(self, image, max_results: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., additional_properties: Any | None = ...): ...
    def safe_search_detection(self, image, max_results: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., additional_properties: Any | None = ...): ...
