from random import randint

from ..abstractions import Number
from ..nodes.NumberNode import NumberNode


class RandomNumberNode(NumberNode):
    from_number: Number
    to_number: Number
    
    def __init__(self, from_number: Number, to_number: Number) -> None:
        super().__init__()

        self.from_number = from_number
        self.to_number = to_number
        self.random_int = None

        self.reset()

    def get_value(self) -> int:
        return self.random_int

    def reset(self) -> None:
        super().reset()
        
        self.random_int = randint(int(self.from_number), int(self.to_number))
