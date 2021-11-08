import abc

ABC = abc.ABC

class K8SModel(ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def attach_to_pod(self, pod): ...
    def as_dict(self): ...

def append_to_pod(pod, k8s_objects): ...
