from pygame.surface import Surface, SurfaceType

from .TextTemplateElement import TextTemplateElement

from ..abstractions import NodeSlotType
from ..template_element import TemplateElement


class TextLineTemplateElement(TemplateElement):
    text: str

    def __init__(self, text: str, *node_slots: tuple[NodeSlotType, ...]) -> None:
        super().__init__()
        
        self.node_slots = node_slots
        self.text_line = TextTemplateElement(text, *node_slots)

    def render(self, sy: int = 0) -> SurfaceType:
        if self.text_line.template is None:
            self.text_line.template = self.template

        line = self.text_line.render()
        surface = Surface((line.get_size()[0] + 10, 25))

        surface.fill(self.template.color)
        surface.blit(line, (5, 1))

        self.template.width = max(self.template.width or 0, surface.get_size()[0])

        return surface
