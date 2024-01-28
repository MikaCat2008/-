from ..abstractions import Blocks, String
from ..block import StructureBlock
from ..listener import Listener
from ..block_iterator import BlockIterator


@StructureBlock
@Listener("key")
class OnKeyPressBlock(BlockIterator):
    key: String
    blocks: Blocks
    execute_key: str

    def __init__(self, key: String, blocks: Blocks) -> None:
        super().__init__()

        self.key = key
        self.blocks = blocks
        self.execute_key = ""

    def execute(self, key: str) -> bool:
        if not self.execute_key == str(self.key):
            self.execute_key = key

        return True

    def iter(self) -> None:
        if str(self.key) == self.execute_key:
            self.execute_key = ""

            return self.blocks
        return []

    def stop(self) -> None:
        super().stop()

        for block in self.blocks:
            block.stop()
