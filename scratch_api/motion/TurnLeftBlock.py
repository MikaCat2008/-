from ..abstractions import Number
from ..block import Block


class TurnLeftBlock(Block):
    angle: Number

    def __init__(self, *args: tuple[Number]) -> None:
        super().__init__(args)

        self.angle = args[0]

    def execute(self) -> bool:
        self.sprite.direction += float(self.angle)

        return True
