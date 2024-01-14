from ..abstractions import Blocks, Boolean
from ..block import StructureBlock
from ..block_iterator import BlockIterator


@StructureBlock
class RepeatUntilBlock(BlockIterator):
    condition: Boolean
    blocks: Blocks

    def __init__(self, condition: Boolean, blocks: Blocks) -> None:
        super().__init__()

        self.condition = condition
        self.blocks = blocks

    def execute(self) -> bool:
        return bool(self.condition)

    def iter(self) -> None:
        if not bool(self.condition):
            return self.blocks
        return []

    def stop(self) -> None:
        super().stop()
        
        for block in self.blocks:
            block.stop()
