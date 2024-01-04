from ..abstractions import Number
from ..block import Block


class WaitBlock(Block):
    freeze_time: Number

    def __init__(self, *args: tuple[Number]) -> None:
        super().__init__(args)

        self.freeze_time = args[0]

    def execute(self) -> bool:
        self.main_block.freeze(self.freeze_time)

        return True
