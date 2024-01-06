from ..abstractions import Boolean
from ..nodes.BooleanNode import BooleanNode


class AndNode(BooleanNode):
    a: Boolean
    b: Boolean

    def __init__(self, a: Boolean, b: Boolean) -> None:
        super().__init__()

        self.a = a
        self.b = b

    def get_value(self) -> bool:
        return bool(self.a) and bool(self.b)
