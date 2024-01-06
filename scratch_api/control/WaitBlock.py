from ..abstractions import Number
from ..block import Block


class WaitBlock(Block):
    freeze_time: Number

    def __init__(self, freeze_time: Number) -> None:
        super().__init__()

        self.freeze_time = freeze_time

    def execute(self) -> bool:
        self.main_block.freeze(self.freeze_time)

        return True
