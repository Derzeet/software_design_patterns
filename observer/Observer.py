from __future__ import annotations
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass



class User(Observer):
    def __init__(self, email) -> None:
        self.email = email


    def update(self, subject: Subject) -> None:
        if self.email in subject._state.keys():
            print(f"There is a new message for {self.email}, that says: {subject._state[self.email]}")
