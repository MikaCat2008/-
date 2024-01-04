from ..abstractions import Number
from ..block import Block


class ChangeYByBlock(Block):
    y: Number

    def __init__(self, *args: tuple[Number]) -> None:
        super().__init__(args)

        self.y = args[0]

    def execute(self) -> bool:
        x, y = self.sprite.coords

        self.sprite.coords = x, y - float(self.y)

        return True
