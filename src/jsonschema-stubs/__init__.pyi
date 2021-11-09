from typing import Any, Dict, List, Union


class ValidationError(Exception):
    ...


def validate(
        input: Union[Dict[str, Any], List[Any]],
        schema: Dict[str, Any],
        ) -> None: ...
