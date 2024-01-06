from ..abstractions import Number
from ..block import Block


class TurnLeftBlock(Block):
    angle: Number

    def __init__(self, angle: Number) -> None:
        super().__init__()

        self.angle = angle

    def execute(self) -> bool:
        self.sprite.set_direction(self.sprite.direction + float(self.angle))

        return True
