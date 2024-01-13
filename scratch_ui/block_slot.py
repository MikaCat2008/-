from .abstractions import BlockType, BlockSlotType

from scratch_api.abstractions import BlockType as GameBlockType


class BlockSlot(BlockSlotType):
    def __init__(self, game_blocks: list[GameBlockType], parent_block: BlockType) -> None:
        self.blocks = []
        self.game_blocks = game_blocks
        self.parent_block = parent_block
    
    def add(self, block: BlockType) -> None:
        self.blocks.append(block)
        self.game_blocks.append(block.game_block)
