import abc
from abc import abstractmethod
from typing import Any

class BaseDag(metaclass=abc.ABCMeta):
    __metaclass__: Any
    @property
    @abc.abstractmethod
    def dag_id(self): ...
    @property
    @abc.abstractmethod
    def task_ids(self): ...
    @property
    @abc.abstractmethod
    def full_filepath(self): ...
    @abstractmethod
    def concurrency(self): ...
    @abstractmethod
    def pickle_id(self): ...

class BaseDagBag(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def dag_ids(self): ...
    @abstractmethod
    def get_dag(self, dag_id): ...
