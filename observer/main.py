from Subject import Inbox
from Observer import User

if __name__ == "__main__":
    subject = Inbox()
    user = User("cocarecu@gmail.com")
    subject.addEmail(user)

    subject.updateInbox("cocarecu@gmail.com", "Hello Cocarecu")
    subject.updateInbox("derzeet@gmail.com", "Hello 2")
