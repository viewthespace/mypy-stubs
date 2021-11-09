from . import BaseResource as BaseResource, Stack as Stack

class Slug(BaseResource):
    order_by: str
    def __init__(self) -> None: ...
