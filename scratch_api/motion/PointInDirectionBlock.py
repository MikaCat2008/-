from ..abstractions import Number
from ..block import Block


class PointInDirectionBlock(Block):
    direction: Number

    def __init__(self, *args: tuple[Number]) -> None:
        super().__init__(args)

        self.direction = args[0]

    def execute(self) -> bool:
        self.sprite.set_direction(float(self.direction))

        return True
