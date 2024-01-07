from ..abstractions import Number
from ..motion_block import MotionBlock


class ChangeXByBlock(MotionBlock):
    x: Number

    def __init__(self, x: Number) -> None:
        super().__init__()

        self.x = x

    def execute(self) -> bool:
        x, y = self.sprite.coords

        self.sprite.coords = x + float(self.x), y

        return True
