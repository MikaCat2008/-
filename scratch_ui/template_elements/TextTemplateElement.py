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
        node = self.node_slots[i]
        surface = node.render()
        node.rendered = surface
        
        return surface

    def render_line(self) -> SurfaceType:
        lines = re.split(r"<\d>", self.text)
        len_lines = len(lines)
        surfaces: list[SurfaceType] = [None] * (len_lines * 2 - 1)

        for i, text in enumerate(lines):
            surfaces[i * 2] = text_render(text)

            if i + 1 < len_lines:
                surfaces[i * 2 + 1] = self.node_render(i)

        surface = Surface((
            sum(element.get_width() for element in surfaces), 25
        ), SRCALPHA, 32)
        
        w = 0
        for i, _surface in enumerate(surfaces):
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
