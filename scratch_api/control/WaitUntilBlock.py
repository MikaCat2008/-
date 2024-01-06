from ..abstractions import Number
from ..block import Block


class WaitUntilBlock(Block):
    condition: Number

    def __init__(self, condition: Number) -> None:
        super().__init__()

        self.condition = condition

    def execute(self) -> bool:
        return bool(self.condition)
