from scratch_api.abstractions import Number
from ..nodes.BooleanNode import BooleanNode


class EqualsToNode(BooleanNode):
    a: Number
    b: Number

    def __init__(self, a: Number, b: Number) -> None:
        super().__init__()

        self.a = a
        self.b = b

    def get_value(self) -> bool:
        return float(self.a) == float(self.b)
