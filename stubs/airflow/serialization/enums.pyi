from enum import Enum

class Encoding(str, Enum):
    TYPE: str
    VAR: str

class DagAttributeTypes(str, Enum):
    DAG: str
    OP: str
    DATETIME: str
    TIMEDELTA: str
    TIMEZONE: str
    RELATIVEDELTA: str
    DICT: str
    SET: str
    TUPLE: str
