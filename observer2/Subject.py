from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def add(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Shop(Subject):
    _state = []

    _observers: List[Observer] = []

    def add(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def updateShop(self, device) -> None:
        self._state.append(device)
        print(f"Our device list has been updated: ")
        for i in range(len(self._state)):
            print(self._state[i])
        self.notify()