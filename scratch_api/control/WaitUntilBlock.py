from ..abstractions import Number
from ..block import Block


class WaitUntilBlock(Block):
    condition: Number

    def __init__(self, *args: tuple[Number]) -> None:
        super().__init__(args)

        self.condition = args[0]

    def execute(self) -> bool:
        return bool(self.condition)
