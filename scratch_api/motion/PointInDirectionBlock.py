from ..abstractions import Number
from ..motion_block import MotionBlock


class PointInDirectionBlock(MotionBlock):
    direction: Number

    def __init__(self, direction: Number) -> None:
        super().__init__()

        self.direction = direction

    def execute(self) -> bool:
        self.sprite.set_direction(float(self.direction))

        return True
