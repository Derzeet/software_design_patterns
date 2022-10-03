from Component import Component

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def execute(self) -> str:
        return self._component.execute()

class Jeans(Decorator):
    def execute(self) -> str:
        return f"Jeans_are_worn_by({self.component.execute()})"

class Hat(Decorator):
    def execute(self) -> str:
        return f"Hat_is_worn_by({self.component.execute()})"