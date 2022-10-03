from abc import ABC, abstractmethod
from Strategy import mail

class Component(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass

class Email(Component):
    def create(self, email, text, reciever):
        self.email = email
        self.text = text
        self.reciever = reciever

    def execute(self) -> str:
        return "email"

    def strategy(self, strategy: mail) -> None:
        self.strategy = strategy

    def send(self, email, list, text, reciever, emails) -> str:
        return self.strategy.sendEmail(email, list, text, reciever, emails)