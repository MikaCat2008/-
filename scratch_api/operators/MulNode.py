from ..abstractions import Number
from ..nodes.NumberNode import NumberNode


class MulNode(NumberNode):
    a: Number
    b: Number
    
    def __init__(self, a: Number, b: Number) -> None:
        super().__init__()

        self.a = a
        self.b = b

    def get_value(self) -> float:
        return float(self.a) * float(self.b)
