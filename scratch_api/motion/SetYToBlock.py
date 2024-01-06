from ..abstractions import Number
from ..block import Block


class SetYToBlock(Block):
    y: Number

    def __init__(self, y: Number) -> None:
        super().__init__()

        self.y = y

    def execute(self) -> bool:
        x, _ = self.sprite.coords

        self.sprite.coords = x, float(self.y)

        return True
