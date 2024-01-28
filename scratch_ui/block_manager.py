from .abstractions import BlockType, SpriteType, GameBlockType, BlockManagerType
from .objects import objects


class BlockManager(BlockManagerType):
    def create_block(
        self,
        sprite: SpriteType,
        coords: tuple[int, int],
        game_block: GameBlockType
    ) -> BlockType:
        if sprite:
            game_block.sprite = sprite.game_sprite

        return objects[type(game_block)](sprite, coords, game_block)


block_manager = BlockManager()
