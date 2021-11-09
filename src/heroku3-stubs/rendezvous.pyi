from typing import Any

class InvalidResponseFromRendezVous(Exception): ...

class Rendezvous:
    url: Any
    hostname: Any
    port: Any
    secret: Any
    cert: Any
    data: str
    printout: Any
    def __init__(self, url, printout: bool = ...) -> None: ...
    def start(self): ...
