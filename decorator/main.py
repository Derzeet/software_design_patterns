from Component import Component, Person
from Decorator import Jeans, Hat

def client_code(component: Component) -> None:
    print(f"RESULT: {component.execute()}", end="")

if __name__ == "__main__":
    person = Person()
    print("Client: I've got a person: ")
    client_code(person)
    print("\n")

    jeans = Jeans(person)
    Hat = Hat(jeans)
    print("Client: Now I've got a decorated person:")
    client_code(Hat)