from ..abstractions import StringNodeType
from ..node import Node


class StringNode(StringNodeType, Node):
    def __init__(self, value: str = "") -> None:
        super().__init__()

        self.value = value

    def get_value(self) -> str:
        return self.value

    def __str__(self) -> str:
        return str(self.get_value())
