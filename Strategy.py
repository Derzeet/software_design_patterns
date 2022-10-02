from abc import ABC, abstractmethod

class SignIn(ABC):
    @abstractmethod
    def do_signin(self, email, password, list):
        pass

class mail(ABC):
    @abstractmethod
    def sendEmail(self, email, list, text, reciever, emails):
        pass