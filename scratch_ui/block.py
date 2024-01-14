from pygame.surface import SurfaceType

from .abstractions import BlockType, SpriteType, BlockSlotType

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
        self.rendered = None

        self.slots = []
        self.template = None

    def init(self) -> None:
        ...

    def add_block(self, block: BlockType, slot: int) -> None:
        self.slots[slot].add(block)
        block.init()

        return block
    
    def get_child(self, mx: int, my: int) -> tuple[BlockType, int, int]:
        for slot in self.slots:
            y = 25
            if isinstance(slot, BlockSlotType):
                for i, block in enumerate(slot.blocks):
                    bx, by = block.coords
                    bw, bh = block.rendered.get_size()

                    if bx <= mx <= bx + bw and by <= my <= by + bh:
                        indent = 0
                        if slot.indent:
                            indent = 20

                        child, cx, cy = block.get_child(mx - indent, my - y)
                        
                        return child, cx + indent, cy + y
                    y += bh

        return self, 0, 0

    def render(self) -> SurfaceType:
        self.rendered = self.template.render()
        
        return self.rendered
