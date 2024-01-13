from pygame.surface import Surface, SurfaceType

from .abstractions import BlockType, SpriteType

from scratch_api.block import BlockType as GameBlockType


class Block(BlockType):
    def __init__(
        self, 
        sprite: SpriteType, 
        coords: tuple[int, int],
        game_block: GameBlockType
    ) -> None:
        self.sprite = sprite
        self.coords = coords
        self.game_block = game_block

        self.slots = []
        self.template = None

    def init(self) -> None:
        ...

    def add_block(self, block: BlockType, slot: int) -> None:
        self.slots[slot].add(block)
        block.init()

        return block
    
    def render(self) -> SurfaceType:
        return self.template.render()
