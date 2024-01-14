from pygame.surface import SurfaceType

from .abstractions import BlockType, SpriteType, BlockSlotType, TemplateElementType
from .template_elements import BlocksTemplateElement

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
        self.slot = None

        self.slots = []
        self.template = None

    def init(self) -> None:
        ...

    def add_block(self, block: BlockType, slot: int) -> None:
        self.slots[slot].add(block)
        block.init()

        return block

    def get_template_element_by_y(self, y: int) -> tuple[TemplateElementType, int, int]:        
        h = 0
        for template_element in self.template.template_elements:
            tew, teh = template_element.rendered.get_size()

            if h <= y <= h + teh:
                return template_element, tew, h

            h += teh

    def get_slot_by_coords(self, x: int, y: int) -> tuple[BlockSlotType, int, int]:
        template_element, w, h = self.get_template_element_by_y(y)

        if isinstance(template_element, BlocksTemplateElement):
            if 20 <= x:
                return template_element.slot, w, h
        return None, None, None

    def get_child(self, mx: int, my: int) -> tuple[BlockType, int, int]:
        for slot in self.slots:
            y = 25
            if isinstance(slot, BlockSlotType):
                for block in slot.blocks:
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

    def is_event(self) -> bool:
        return not self.game_block.event is None

    def is_iterable(self) -> bool:
        return any(isinstance(slot, BlockSlotType) for slot in self.slots)

    def render(self) -> SurfaceType:
        self.rendered = self.template.render()
        
        return self.rendered
