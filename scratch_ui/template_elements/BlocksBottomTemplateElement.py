from pygame import SRCALPHA
from pygame.draw import rect
from pygame.surface import Surface, SurfaceType

from ..template_element import TemplateElementType


class BlocksBottomTemplateElement(TemplateElementType):
    def render(self, sy: int = 0) -> SurfaceType:
        surface = Surface((self.template.width, 20), SRCALPHA, 32)

        rect(surface, self.color, (0, 0, self.template.width, 20))

        return surface
