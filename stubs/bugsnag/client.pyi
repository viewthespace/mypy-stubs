import typing as T


class Client:
    def capture(
            self,
            exceptions: T.Optional[T.List[BaseException]] = None,
            **options: T.Any,
            ) -> T.ContextManager[None]: ...
