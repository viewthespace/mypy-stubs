import ssl
from typing import Callable, List, Union

from .fetcher import ConsumerRecord


class KafkaConsumer:
    def __init__(
            self,
            topics: Union[List[str], str] = None,
            bootstrap_servers: Union[List[str], str] = None,
            auto_offset_reset: str = None,
            consumer_timeout_ms: int = None,
            group_id: str = None,
            security_protocol: str = None,
            api_version: tuple = None,
            ssl_cafile: str = None,
            ssl_certfile: str = None,
            ssl_check_hostname: bool = None,
            ssl_context: ssl.SSLContext = None,
            ssl_keyfile: str = None,
            value_deserializer: Callable[[bytes], bytes] = None,
            ) -> None:
        pass

    def __iter__(self) -> 'KafkaConsumer':
        pass

    def __next__(self) -> ConsumerRecord:
        pass

    def bootstrap_connected(self) -> bool:
        pass
