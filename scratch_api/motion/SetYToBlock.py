from ..abstractions import Number
from ..motion_block import MotionBlock


class SetYToBlock(MotionBlock):
    y: Number

    def __init__(self, y: Number) -> None:
        super().__init__()

        self.y = y

    def execute(self) -> bool:
        x, _ = self.sprite.coords

        self.sprite.coords = x, float(self.y)

        return True
