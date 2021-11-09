from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class MongoHook(BaseHook):
    conn_type: str
    mongo_conn_id: Any
    connection: Any
    extras: Any
    client: Any
    uri: Any
    def __init__(self, conn_id: str = ..., *args, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def get_conn(self): ...
    def close_conn(self) -> None: ...
    def get_collection(self, mongo_collection, mongo_db: Any | None = ...): ...
    def aggregate(self, mongo_collection, aggregate_query, mongo_db: Any | None = ..., **kwargs): ...
    def find(self, mongo_collection, query, find_one: bool = ..., mongo_db: Any | None = ..., **kwargs): ...
    def insert_one(self, mongo_collection, doc, mongo_db: Any | None = ..., **kwargs): ...
    def insert_many(self, mongo_collection, docs, mongo_db: Any | None = ..., **kwargs): ...
    def update_one(self, mongo_collection, filter_doc, update_doc, mongo_db: Any | None = ..., **kwargs): ...
    def update_many(self, mongo_collection, filter_doc, update_doc, mongo_db: Any | None = ..., **kwargs): ...
    def replace_one(self, mongo_collection, doc, filter_doc: Any | None = ..., mongo_db: Any | None = ..., **kwargs): ...
    def replace_many(self, mongo_collection, docs, filter_docs: Any | None = ..., mongo_db: Any | None = ..., upsert: bool = ..., collation: Any | None = ..., **kwargs): ...
    def delete_one(self, mongo_collection, filter_doc, mongo_db: Any | None = ..., **kwargs): ...
    def delete_many(self, mongo_collection, filter_doc, mongo_db: Any | None = ..., **kwargs): ...