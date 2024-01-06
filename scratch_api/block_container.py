from .abstractions import Blocks
from .block_iterator import BlockIterator


class BlockContainer(BlockIterator):
    def iter(self) -> Blocks:
        return []
