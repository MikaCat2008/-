from pygame import SRCALPHA
from pygame.draw import rect
from pygame.surface import Surface, SurfaceType

from ..abstractions import BlockSlotType
from ..template_element import TemplateElement


class BlocksTemplateElement(TemplateElement):
    slot: BlockSlotType
    indent: bool
    
    def __init__(self, slot: BlockSlotType, indent: bool) -> None:
        super().__init__()

        self.slot = slot
        self.indent = indent

    def render(self) -> SurfaceType:
        surfaces = [None] * len(self.slot.blocks)

        for i, block in enumerate(self.slot.blocks):
            surfaces[i] = block.render()

        sw, sh = self.template.width, self.indent * 15
        for _surface in surfaces:
            w, h = _surface.get_size()
            
            sw = max(w, sw)
            sh += h

        surface = Surface((sw, sh), SRCALPHA, 32)
        
        y = 0
        for _surface in surfaces:
            surface.blit(_surface, (self.indent * 20, y))

            y += _surface.get_size()[1]

        if self.indent:
            rect(surface, self.color, (0, 0, 20, y))
            rect(surface, self.color, (0, y, 20, 15))

        return surface
