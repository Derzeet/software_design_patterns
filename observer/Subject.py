from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def addEmail(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def removeEmail(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Inbox(Subject):
    _state = {}

    _observers: List[Observer] = []

    def addEmail(self, observer: Observer) -> None:
        self._observers.append(observer)

    def removeEmail(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def updateInbox(self, email, text) -> None:
        self._state[email] = text
        print(f"Inbox has recieved a new message: {self._state}")
        self.notify()