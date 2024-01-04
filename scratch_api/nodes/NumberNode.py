from ..abstractions import NumberNodeType
from ..node import Node


class NumberNode(NumberNodeType, Node):
    def __init__(self, value: float = 0.0) -> None:
        super().__init__()

        self.value = value

    def get_value(self) -> float:
        return self.value

    def __int__(self) -> int:
        return int(self.get_value())

    def __float__(self) -> float:
        return float(self.get_value())
