from . import BaseResource as BaseResource, User as User
from .buildpack import Buildpack as Buildpack
from .slug import Slug as Slug
from .sourceblob import SourceBlob as SourceBlob

class Build(BaseResource):
    def __init__(self) -> None: ...
