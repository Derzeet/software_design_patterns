import Strategy

class Account():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_signing(self, email, password, list) -> str:
        return self._strategy.do_signin(email, password, list)

class Email():
    def create(self, email, text, reciever):
        self.email = email
        self.text = text
        self.reciever = reciever

    def strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def send(self, email, list, text, reciever, emails) -> str:
        return self.strategy.sendEmail(email, list, text, reciever, emails)
