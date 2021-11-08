from typing import List, NamedTuple, Optional, Tuple

ConsumerRecord = NamedTuple('ConsumerRecord', [
    ('topic', str),
    ('partition', int),
    ('offset', int),
    ('timestamp', int),
    ('timestamp_type', int),
    ('key', Optional[bytes]),
    ('value', Optional[bytes]),
    ('headers', Optional[List[Tuple[str, bytes]]]),
    ('checksum', None),  # Deprecated, so disallow usage by forcing None
    ('serialized_key_size', int),
    ('serialized_value_size', int),
    ('serialized_header_size', int),
    ])
