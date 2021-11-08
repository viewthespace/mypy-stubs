from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from airflow.exceptions import AirflowException as AirflowException
from typing import Any

class S3Hook(AwsHook):
    def get_conn(self): ...
    @staticmethod
    def parse_s3_url(s3url): ...
    def check_for_bucket(self, bucket_name): ...
    def get_bucket(self, bucket_name): ...
    def create_bucket(self, bucket_name, region_name: Any | None = ...) -> None: ...
    def check_for_prefix(self, bucket_name, prefix, delimiter): ...
    def list_prefixes(self, bucket_name, prefix: str = ..., delimiter: str = ..., page_size: Any | None = ..., max_items: Any | None = ...): ...
    def list_keys(self, bucket_name, prefix: str = ..., delimiter: str = ..., page_size: Any | None = ..., max_items: Any | None = ...): ...
    def check_for_key(self, key, bucket_name: Any | None = ...): ...
    def get_key(self, key, bucket_name: Any | None = ...): ...
    def read_key(self, key, bucket_name: Any | None = ...): ...
    def select_key(self, key, bucket_name: Any | None = ..., expression: str = ..., expression_type: str = ..., input_serialization: Any | None = ..., output_serialization: Any | None = ...): ...
    def check_for_wildcard_key(self, wildcard_key, bucket_name: Any | None = ..., delimiter: str = ...): ...
    def get_wildcard_key(self, wildcard_key, bucket_name: Any | None = ..., delimiter: str = ...): ...
    def load_file(self, filename, key, bucket_name: Any | None = ..., replace: bool = ..., encrypt: bool = ..., gzip: bool = ..., acl_policy: Any | None = ...) -> None: ...
    def load_string(self, string_data, key, bucket_name: Any | None = ..., replace: bool = ..., encrypt: bool = ..., encoding: str = ..., acl_policy: Any | None = ...) -> None: ...
    def load_bytes(self, bytes_data, key, bucket_name: Any | None = ..., replace: bool = ..., encrypt: bool = ..., acl_policy: Any | None = ...) -> None: ...
    def load_file_obj(self, file_obj, key, bucket_name: Any | None = ..., replace: bool = ..., encrypt: bool = ..., acl_policy: Any | None = ...) -> None: ...
    def copy_object(self, source_bucket_key, dest_bucket_key, source_bucket_name: Any | None = ..., dest_bucket_name: Any | None = ..., source_version_id: Any | None = ..., acl_policy: str = ...): ...
    def delete_objects(self, bucket, keys): ...
