from ..abstractions import Blocks
from ..block import StructureBlock
from ..block_iterator import BlockIterator


@StructureBlock
class ForeverBlock(BlockIterator):
    blocks: Blocks

    def __init__(self, *args: tuple[Blocks]) -> None:
        super().__init__(args)

        self.blocks = args[0]

    def execute(self) -> bool:
        return False

    def iter(self) -> None:
        return self.blocks
