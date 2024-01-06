from ..abstractions import Blocks, Boolean
from ..block import StructureBlock
from ..block_iterator import BlockIterator


@StructureBlock
class IfThenElseBlock(BlockIterator):
    condition: Boolean
    then_blocks: Blocks
    else_blocks: Blocks

    def __init__(self, *args: tuple[Boolean, Blocks, Blocks]) -> None:
        super().__init__()

        self.condition = args[0]
        self.then_blocks = args[1]
        self.else_blocks = args[2]

    def execute(self) -> bool:
        return True

    def iter(self) -> None:
        if bool(self.condition):
            return self.then_blocks
        return self.else_blocks
