from typing import Any, Dict, IO

from .io import DatumReader, DatumWriter
from .schema import Schema


class DataFileReader:
    def __init__(
            self,
            reader: IO[bytes],
            datum_reader: DatumReader,
            ) -> None:
        pass

    def __iter__(self) -> 'DataFileReader':
        pass

    def __next__(self) -> Dict[str, Any]:
        pass

    def close(self) -> None:
        pass


class DataFileWriter:
    def __init__(
            self,
            writer: IO[bytes],
            datum_writer: DatumWriter,
            schema: Schema,
            ) -> None:
        pass

    def append(self, datum: Dict[str, Any]) -> None:
        pass

    def flush(self) -> None:
        pass
