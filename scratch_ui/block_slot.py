from .abstractions import BlockType, BlockSlotType

from scratch_api.abstractions import BlockType as GameBlockType


class BlockSlot(BlockSlotType):
    def __init__(self, game_blocks: list[GameBlockType]) -> None:
        self.blocks = []
        self.indent = False
        self.game_blocks = game_blocks
    
    def add(self, block: BlockType) -> None:
        self.blocks.append(block)
        self.game_blocks.append(block.game_block)
