import re

from pygame import SRCALPHA
from pygame.surface import Surface, SurfaceType

from ..abstractions import NodeSlotType
from ..font import text_render
from ..template_element import TemplateElement


class TextTemplateElement(TemplateElement):
    text: str

    def __init__(self, text: str, *node_slots: tuple[NodeSlotType, ...]) -> None:
        super().__init__()
        
        self.text = text
        self.node_slots: tuple[NodeSlotType, ...] = node_slots

    def node_render(self, i: int) -> SurfaceType:
        node_slot = self.node_slots[i]
        surface = node_slot.render()
        node_slot.node.rendered = surface
        
        return surface

    def render_line(self) -> SurfaceType:
        lines = re.split(r"<\d>", self.text)
        len_lines = len(lines)
        surfaces: list[SurfaceType] = [None] * (len_lines * 2 - 1)

        w = 0
        for i, text in enumerate(lines):
            surface = text_render(text)
            
            surfaces[i * 2] = surface
            w += surface.get_width()

            if i + 1 < len_lines:
                surface = self.node_render(i)

                surfaces[i * 2 + 1] = surface
                self.node_slots[i].node.coords = (w, 0)
                w += surface.get_width()

        surface = Surface((
            sum(element.get_width() for element in surfaces), 25
        ), SRCALPHA, 32)
        
        w = 0
        for _surface in surfaces:
            surface.blit(_surface, (w, 0))
            
            w += _surface.get_width()

        return surface

    def render(self, sy: int = 0) -> SurfaceType:
        line = self.render_line()
        surface = Surface((line.get_size()[0] + 10, 25))

        surface.fill(self.color)
        surface.blit(line, (5, 1))

        self.template.width = max(self.template.width or 0, surface.get_size()[0])

        return surface
