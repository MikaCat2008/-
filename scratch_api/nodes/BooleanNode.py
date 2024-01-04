from ..abstractions import BooleanNodeType
from ..node import Node


class BooleanNode(BooleanNodeType, Node):
    def __init__(self, value: bool = False) -> None:
        super().__init__()

        self.value = value

    def get_value(self) -> bool:
        return self.value

    def __bool__(self) -> bool:
        return bool(self.get_value())
