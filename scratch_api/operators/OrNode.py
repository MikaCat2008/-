from ..abstractions import Boolean
from ..nodes.BooleanNode import BooleanNode


class OrNode(BooleanNode):
    a: Boolean
    b: Boolean

    def __init__(self, a: Boolean, b: Boolean) -> None:
        super().__init__()

        self.a = a
        self.b = b

    def get_value(self) -> bool:
        return bool(self.a) or bool(self.b)
