from ..block import Block

from ..stamp import clear


class ClearBlock(Block):
    def execute(self) -> bool:
        clear()

        return True
