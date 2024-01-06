from ..abstractions import Number
from ..block import Block


class SetRotationStyleBlock(Block):
    rotation_style: Number

    def __init__(self, *args: tuple[Number]) -> None:
        super().__init__(args)

        self.rotation_style = args[0]

    def execute(self) -> bool:
        self.sprite.rotation_style = int(self.rotate_style)

        return True
