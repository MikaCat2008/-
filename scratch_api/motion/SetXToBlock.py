from ..abstractions import Number
from ..block import Block


class SetXToBlock(Block):
    x: Number

    def __init__(self, x: Number) -> None:
        super().__init__()

        self.x = x

    def execute(self) -> bool:
        _, y = self.sprite.coords

        self.sprite.coords = float(self.x), y

        return True
