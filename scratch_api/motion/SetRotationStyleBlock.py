from ..abstractions import Number
from ..motion_block import MotionBlock


class SetRotationStyleBlock(MotionBlock):
    rotation_style: Number

    def __init__(self, rotation_style: Number) -> None:
        super().__init__()

        self.rotation_style = rotation_style

    def execute(self) -> bool:
        self.sprite.rotation_style = int(self.rotation_style)

        return True
