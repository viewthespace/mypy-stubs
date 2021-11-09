from airflow.contrib.hooks.mongo_hook import MongoHook as MongoHook
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class MongoToS3Operator(BaseOperator):
    template_fields: Any
    mongo_conn_id: Any
    s3_conn_id: Any
    mongo_db: Any
    mongo_collection: Any
    mongo_query: Any
    is_pipeline: Any
    s3_bucket: Any
    s3_key: Any
    replace: Any
    def __init__(self, mongo_conn_id, s3_conn_id, mongo_collection, mongo_query, s3_bucket, s3_key, mongo_db: Any | None = ..., replace: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
    @staticmethod
    def transform(docs): ...
