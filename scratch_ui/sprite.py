from .abstractions import BlockType, SpriteType
from .block_manager import block_manager

from scratch_api.block import BlockType as GameBlockType
from scratch_api.sprite import SpriteType as GameSpriteType


class Sprite(SpriteType):
    def __init__(
        self, 
        game_sprite: GameSpriteType,
        blocks: list[BlockType]
    ) -> None:
        self.game_sprite = game_sprite
        self.blocks = blocks

    def add_block(self, coords: tuple[int, int], game_block: GameBlockType) -> None:
        for block in self.blocks:
            if False:
            # if block.can_add_block(coords, game_block):
                block.add_block(coords, game_block)
                
                break
        else:
            block = block_manager.create_block(
                self,
                coords,
                game_block
            )

            block.deep = 0
            block.init()

            self.blocks.append(block)
        
        return block

