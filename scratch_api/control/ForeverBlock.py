from ..abstractions import Blocks
from ..block import StructureBlock
from ..block_iterator import BlockIterator


@StructureBlock
class ForeverBlock(BlockIterator):
    blocks: Blocks

    def __init__(self, blocks: Blocks) -> None:
        super().__init__()

        self.blocks = blocks

    def execute(self) -> bool:
        return False

    def iter(self) -> None:
        return self.blocks

    def stop(self) -> None:
        super().stop()
        
        for block in self.blocks:
            block.stop()
