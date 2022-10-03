from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass

class Person(Component):
    def execute(self) -> str:
        return "Person"

