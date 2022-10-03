from abc import ABC, abstractmethod

class mail(ABC):
    @abstractmethod
    def sendEmail(self, email, list, text, reciever, emails):
        pass