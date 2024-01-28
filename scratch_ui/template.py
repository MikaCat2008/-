from pygame import SRCALPHA
from pygame.surface import Surface, SurfaceType

from .abstractions import TemplateType, TemplateElementType


class Template(TemplateType):
    def __init__(
        self, 
        template_elements: list[TemplateElementType], 
        color: tuple[int, int, int],
        mode: str = "block"
    ) -> None:
        self.width = None
        self.template_elements = template_elements
        self.color = color
        self.mode = mode

        for template_element in template_elements:
            template_element.template = self

    def get_surfaces(self) -> list[SurfaceType]:
        if self.mode == "block":
            surfaces = [None] * len(self.template_elements)

            y = 0
            for i, template_element in enumerate(self.template_elements):
                surface = template_element.render(y)

                surfaces[i] = surface
                template_element.rendered = surface
                y += surface.get_height()
        else:
            surfaces = self.template_elements[0].get_surfaces()

        return surfaces

    def render(self) -> SurfaceType:
        surfaces = self.get_surfaces()
        
        sw, sh, w, y = 0, 0, 0, 0

        if self.mode == "block":
            for _surface in surfaces:
                w, h = _surface.get_size()
                
                sw = max(w, sw)
                sh += h
            
            surface = Surface((sw, sh), SRCALPHA, 32)
            
            for _surface in surfaces:
                surface.blit(_surface, (0, y))

                y += _surface.get_height()
        else:
            for _surface in surfaces:
                sw += _surface.get_width()

            surface = Surface((sw, 23), SRCALPHA, 32)
            surface.fill(self.color)

            for _surface in surfaces:
                surface.blit(_surface, (w, 0))

                w += _surface.get_width()

        return surface
