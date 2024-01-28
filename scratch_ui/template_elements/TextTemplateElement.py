import re

from pygame import SRCALPHA
from pygame.surface import Surface, SurfaceType

from ..abstractions import NodeType, NodeSlotType
from ..font import text_render
from ..template_element import TemplateElement


class TextTemplateElement(TemplateElement):
    text: str

    def __init__(
        self, 
        text: str, 
        *node_slots: tuple[NodeType | NodeSlotType, ...],
        color = (255, 255, 255)
    ) -> None:
        super().__init__()
        
        self.text = text
        self.node_slots: tuple[NodeType | NodeSlotType, ...] = node_slots
        self.color = color

    def node_render(self, i: int) -> SurfaceType:
        node_slot = self.node_slots[i]
        
        if isinstance(node_slot, NodeSlotType):
            node = node_slot.node
        else:
            node = node_slot
        
        return node.render()

    def get_surfaces(self) -> list[SurfaceType]:
        lines = re.split(r"<\d>", self.text)
        len_lines = len(lines)
        surfaces: list[SurfaceType] = [None] * (len_lines * 2 - 1)
        
        w = 0
        for i, text in enumerate(lines):
            surface = text_render(text, self.color, indent=1)
            
            surfaces[i * 2] = surface
            w += surface.get_width()

            if i + 1 < len_lines:
                surface = self.node_render(i)

                surfaces[i * 2 + 1] = surface
                self.node_slots[i].node.coords = (w, 0)

                w += surface.get_width()

        return surfaces

    def render(self, sy: int = 0) -> SurfaceType:
        surfaces = self.get_surfaces()

        surface = Surface((
            sum(element.get_width() for element in surfaces), 23
        ), SRCALPHA, 32)
        
        w = 0
        for _surface in surfaces:
            surface.blit(_surface, (w, 0))
            
            w += _surface.get_width()

        return surface
