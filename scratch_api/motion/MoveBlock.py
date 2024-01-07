import math

from ..abstractions import Number
from ..motion_block import MotionBlock


def move(x: float, y: float, d: float, v: float) -> tuple[float, float]:
    x += math.cos(d * math.pi / 180) * v
    y -= math.sin(d * math.pi / 180) * v

    return x, y


class MoveBlock(MotionBlock):
    velocity: Number

    def __init__(self, velocity: Number) -> None:
        super().__init__()

        self.velocity = velocity

    def execute(self) -> bool:
        x, y = self.sprite.coords
        direction = self.sprite.direction

        self.sprite.coords = move(x, y, direction, float(self.velocity))

        return True
