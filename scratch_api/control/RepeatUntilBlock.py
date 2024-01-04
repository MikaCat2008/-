from ..abstractions import Blocks, Boolean
from ..block import StructureBlock
from ..block_iterator import BlockIterator


@StructureBlock
class RepeatUntilBlock(BlockIterator):
    condition: Boolean
    blocks: Blocks

    def __init__(self, *args: tuple[Boolean, Blocks]) -> None:
        super().__init__(args)

        self.condition = args[0]
        self.blocks = args[1]

    def execute(self) -> bool:
        return bool(self.condition)

    def iter(self) -> None:
        if not bool(self.condition):
            return self.blocks
        return []
