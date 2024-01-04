from ..abstractions import Blocks, Number
from ..block import StructureBlock
from ..block_iterator import BlockIterator


@StructureBlock
class RepeatBlock(BlockIterator):
    index: int
    end: Number
    blocks: Blocks

    def __init__(self, *args: tuple[Number, Blocks]) -> None:
        super().__init__(args)

        self.index = 0
        self.end = args[0]
        self.blocks = args[1]

    def execute(self) -> bool:
        self.index += 1

        if self.index == int(self.end):
            self.index = 0
            
            return True
        return False

    def iter(self) -> None:
        return self.blocks
