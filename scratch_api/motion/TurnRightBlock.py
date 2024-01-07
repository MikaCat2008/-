from ..abstractions import Number
from ..motion_block import MotionBlock


class TurnRightBlock(MotionBlock):
    angle: Number

    def __init__(self, angle: Number) -> None:
        super().__init__()

        self.angle = angle

    def execute(self) -> bool:
        self.sprite.set_direction(self.sprite.direction - float(self.angle))

        return True
