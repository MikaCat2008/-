from ..abstractions import Blocks, Boolean
from ..block import StructureBlock
from ..block_iterator import BlockIterator


@StructureBlock
class IfThenElseBlock(BlockIterator):
    condition: Boolean
    then_blocks: Blocks
    else_blocks: Blocks

    def __init__(self, condition: Boolean, then_blocks: Blocks, else_blocks: Blocks) -> None:
        super().__init__()

        self.condition = condition
        self.then_blocks = then_blocks
        self.else_blocks = else_blocks

    def execute(self) -> bool:
        return True

    def iter(self) -> None:
        if bool(self.condition):
            return self.then_blocks
        return self.else_blocks

    def stop(self) -> None:
        super().stop()
        
        for block in self.then_blocks:
            block.stop()
        
        for block in self.else_blocks:
            block.stop()
