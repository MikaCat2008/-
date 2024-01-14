from pygame import SRCALPHA
from pygame.surface import Surface, SurfaceType

from .abstractions import TemplateType, TemplateElementType


class Template(TemplateType):
    def __init__(
        self, 
        template_elements: list[TemplateElementType], 
        color: tuple[int, int, int]
    ) -> None:
        self.width = None
        self.template_elements = template_elements

        for template_element in template_elements:
            template_element.color = color
            template_element.template = self

    def get_surfaces(self) -> list[SurfaceType]:
        surfaces = [None] * len(self.template_elements)

        for i, template_element in enumerate(self.template_elements):
            if i == 0:
                surfaces[i] = template_element.render()
            else:
                surfaces[i] = template_element.render(surfaces[i - 1].get_size()[1])

        return surfaces

    def render(self) -> SurfaceType:
        surfaces = self.get_surfaces()
        
        sw, sh = 0, 0
        for _surface in surfaces:
            w, h = _surface.get_size()
            
            sw = max(w, sw)
            sh += h
        
        surface = Surface((sw, sh), SRCALPHA, 32)
        
        y = 0
        for _surface in surfaces:
            surface.blit(_surface, (0, y))

            y += _surface.get_size()[1]

        return surface
