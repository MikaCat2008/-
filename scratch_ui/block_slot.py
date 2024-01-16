from .abstractions import BlockType, BlockSlotType

from scratch_api.abstractions import BlockType as GameBlockType


class BlockSlot(BlockSlotType):
    def __init__(self, game_blocks: list[GameBlockType]) -> None:
        self.blocks = []
        self.indent = False
        self.game_blocks = game_blocks
    
    def add(self, block: BlockType) -> None:
        block.slot = self
        self.blocks.append(block)
        self.game_blocks.append(block.game_block)

    def index(self, block: BlockType) -> int:
        return self.blocks.index(block)

    def insert(self, index: int, block: BlockType) -> None:
        block.slot = self
        self.blocks.insert(index, block)
        self.game_blocks.insert(index, block.game_block)

    def insert_before(self, block: BlockType, insertable_block: BlockType) -> None:
        self.insert(self.index(block), insertable_block)

    def insert_after(self, block: BlockType, insertable_block: BlockType) -> None:
        self.insert(self.index(block) + 1, insertable_block)
