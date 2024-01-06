from ..abstractions import Number
from ..block import Block


class GoToXYBlock(Block):
    x: Number
    y: Number

    def __init__(self, *args: tuple[Number, Number]) -> None:
        super().__init__(args)

        self.x = args[0]
        self.y = args[1]

    def execute(self) -> bool:
        self.sprite.coords = float(self.x), float(self.y)

        return True
