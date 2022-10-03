from Component import Component, Email
from Decorator import IsSpam, IsImportant

def client_code(component: Component) -> None:
    print(f"RESULT: {component.execute()}", end="")

if __name__ == "__main__":
    email = Email()
    email.create('cocarecu@gmail.com', 'Hello', 'derzeet@gmail.com')
    client_code(email)
    print("\n")

    spam = IsSpam(email)
    print("Client: Now I've got a decorated person:")
    client_code(spam)
