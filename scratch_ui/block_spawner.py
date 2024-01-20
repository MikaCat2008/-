from copy import deepcopy

from pygame.surface import SurfaceType

from .abstractions import BlockType, GameBlockType
from .block_manager import block_manager
from .sprite_manager import sprite_manager


class BlockSpawner:
    def __init__(self, coords: tuple[int, int], game_block: GameBlockType) -> None:
        self.coords = coords
        self.game_block = game_block

        self.block = self.spawn()

    def spawn(self) -> BlockType:
        return block_manager.create_block(
            sprite_manager.selected_sprite,
            self.coords,
            deepcopy(self.game_block)
        )

    def render(self) -> SurfaceType:
        return self.block.render()
