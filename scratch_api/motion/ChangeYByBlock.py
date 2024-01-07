from ..abstractions import Number
from ..motion_block import MotionBlock


class ChangeYByBlock(MotionBlock):
    y: Number

    def __init__(self, y: Number) -> None:
        super().__init__()

        self.y = y

    def execute(self) -> bool:
        x, y = self.sprite.coords

        self.sprite.coords = x, y - float(self.y)

        return True
