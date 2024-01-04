from ..abstractions import Number
from ..block import Block


class ChangeXByBlock(Block):
    x: Number

    def __init__(self, *args: tuple[Number]) -> None:
        super().__init__(args)

        self.x = args[0]

    def execute(self) -> bool:
        x, y = self.sprite.coords

        self.sprite.coords = x + float(self.x), y

        return True
