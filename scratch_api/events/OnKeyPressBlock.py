from ..abstractions import Blocks, String
from ..block import StructureBlock
from ..listener import Listener
from ..block_iterator import BlockIterator


@StructureBlock
@Listener("key")
class OnKeyPressBlock(BlockIterator):
    key: String
    execute_key: str
    blocks: Blocks

    def __init__(self, *args: tuple[String, Blocks]) -> None:
        super().__init__(args)

        self.key = args[0]
        self.execute_key = ""
        self.blocks = args[1]

    def execute(self, key: str) -> bool:
        if not self.execute_key == str(self.key):
            self.execute_key = key

        return True

    def iter(self) -> None:
        if self.key == self.execute_key:
            self.execute_key = ""

            return self.blocks
        return []
