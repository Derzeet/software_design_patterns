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

class IsSpam(Decorator):
    def execute(self) -> str:
        return f"IsSpam({self.component.execute()})"

class IsImportant(Decorator):
    def execute(self) -> str:
        return f"IsImportant({self.component.execute()})"