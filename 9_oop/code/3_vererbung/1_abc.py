"""
Abstract Base Classes
"""

from abc import ABC, abstractmethod


class Worker(ABC):
    """Abstrakte Base Class"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def set_tools(self): ...


class ServiceWorker(Worker):
    """ServiceWorker muss alle abstract methods von Worker implementieren."""

    def set_tools(self, tools):
        pass


s = ServiceWorker("Service Worker Class")
s.set_tools(["hammer", "knife"])
