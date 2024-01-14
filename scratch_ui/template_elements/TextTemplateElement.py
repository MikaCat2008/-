import re

from pygame.surface import Surface, SurfaceType

from ..abstractions import NodeSlotType
from ..font import text_render
from ..template_element import TemplateElement


class TextTemplateElement(TemplateElement):
    text: str

    def __init__(self, text: str, *node_slots: tuple[NodeSlotType, ...]) -> None:
        super().__init__()
        
        self.text = text
        self.node_slots = node_slots

    def get_str(self, match: re.Match) -> str:
        return self.node_slots[int(match.groups()[0])].get_str()

    def format_text(self) -> str:
        return re.sub("<(\d)>", self.get_str, self.text)

    def render(self, sy: int = 0) -> SurfaceType:
        text = text_render(self.format_text())
        surface = Surface((text.get_size()[0] + 10, 25))

        surface.fill(self.color)
        surface.blit(text, (5, 1))

        self.template.width = max(self.template.width or 0, surface.get_size()[0])

        return surface
