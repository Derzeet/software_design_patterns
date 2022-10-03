from Component import Component, Email
from Decorator import IsSpam, IsImportant
from EmailStrategy import sendEmail

def client_code(component: Component) -> None:
    print(f"RESULT: {component.execute()}", end="")

if __name__ == "__main__":
    emails = []
    email = Email()
    email.strategy(sendEmail())
    print(email.send('cocarecu@gmail.com', 'Hello', 'derzeet@gmail.com', emails))

    client_code(email)
    print("\n")

    spam = IsSpam(email)
    print("Client: Now I've got a decorated person:")
    client_code(spam)
    print("\n")
    for email in emails:
        print(email.text, email.reciever, email.email, sep=' ')

