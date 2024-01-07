from ..abstractions import Number
from ..motion_block import MotionBlock


class SetXToBlock(MotionBlock):
    x: Number

    def __init__(self, x: Number) -> None:
        super().__init__()

        self.x = x

    def execute(self) -> bool:
        _, y = self.sprite.coords

        self.sprite.coords = float(self.x), y

        return True
