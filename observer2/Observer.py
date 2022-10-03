from __future__ import annotations
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass



class Client(Observer):

    def update(self, subject: Subject) -> None:
        print(f"Client has recieved an update of your shop list!")
