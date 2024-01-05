from ..node import Node


class VariableNode(Node):
    name: str

    def __init__(self, name: str) -> None:
        super().__init__()

        self.name = name

    def get_value(self) -> object:
        return self.sprite.get_value(self.name)
