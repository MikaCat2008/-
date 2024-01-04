from ..abstractions import Number
from ..block import Block


class SetXToBlock(Block):
    x: Number

    def __init__(self, *args: tuple[Number]) -> None:
        super().__init__(args)

        self.x = args[0]

    def execute(self) -> bool:
        _, y = self.sprite.coords

        self.sprite.coords = float(self.x), y

        return True
