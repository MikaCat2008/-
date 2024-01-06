from ..abstractions import Number
from ..block import Block


class SetRotationStyleBlock(Block):
    rotation_style: Number

    def __init__(self, rotation_style: Number) -> None:
        super().__init__()

        self.rotation_style = rotation_style

    def execute(self) -> bool:
        self.sprite.rotation_style = int(self.rotate_style)

        return True
