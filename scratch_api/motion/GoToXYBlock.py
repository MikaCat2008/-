from ..abstractions import Number
from ..motion_block import MotionBlock


class GoToXYBlock(MotionBlock):
    x: Number
    y: Number

    def __init__(self, x: Number, y: Number) -> None:
        super().__init__()

        self.x = x
        self.y = y

    def execute(self) -> bool:
        self.sprite.coords = float(self.x), float(self.y)

        return True
