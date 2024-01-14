from ..abstractions import Blocks
from ..block import StructureBlock
from ..listener import Listener
from ..block_iterator import BlockIterator


@StructureBlock
@Listener("start")
class OnStartBlock(BlockIterator):
    start: bool
    blocks: Blocks
    
    def __init__(self, blocks: Blocks) -> None:
        super().__init__()

        self.start = False
        self.blocks = blocks

    def execute(self) -> bool:
        self.start = True

        return True

    def iter(self) -> None:
        if self.start:
            self.start = False

            return self.blocks
        return []

    def stop(self) -> None:
        super().stop()
        
        for block in self.blocks:
            block.stop()
