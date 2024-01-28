from copy import deepcopy

from pygame.surface import SurfaceType

from .abstractions import BlockType, SpriteType, GameBlockType, BlockSpawnerType
from .block_manager import block_manager
from .sprite_manager import sprite_manager


class BlockSpawner(BlockSpawnerType):
    def __init__(self, coords: tuple[int, int], game_block: GameBlockType) -> None:
        self.coords = coords
        self.game_block = game_block

        self.block = self.spawn(None)

    def spawn(self, sprite: SpriteType) -> BlockType:
        block = block_manager.create_block(
            sprite_manager.selected_sprite,
            self.coords,
            deepcopy(self.game_block)
        )

        if sprite:
            block.game_block.sprite = sprite.game_sprite
        
        return block

    def render(self) -> SurfaceType:
        return self.block.render()
