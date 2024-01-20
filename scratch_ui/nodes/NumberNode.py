from pygame.surface import Surface, SurfaceType

from ..font import text_render
from ..node import Node

from scratch_api.abstractions import NumberNodeType as NumberGameNodeType


class NumberNode(Node):
    game_node: NumberGameNodeType

    def render(self) -> SurfaceType:
        text = text_render(str(self.game_node.get_value()), (0, 0, 0))
        surface = Surface((text.get_width() + 8, 23))
        
        surface.fill((255, 255, 255))
        surface.blit(text, (4, 1))

        return surface
