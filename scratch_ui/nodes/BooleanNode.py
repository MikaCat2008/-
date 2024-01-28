from pygame.surface import SurfaceType

from ..node import Node
from ..font import text_render

from scratch_api.abstractions import BooleanNodeType as BooleanGameNodeType


class BooleanNode(Node):
    game_node: BooleanGameNodeType

    def get_surfaces(self) -> list[SurfaceType]:
        return [self.render()]

    def render(self) -> SurfaceType:
        if self.template is None:
            self.rendered = text_render(str(self.game_node.get_value()), (0, 0, 0), (255, 255, 255), 3)
        else:
            self.rendered = self.template.render()

        return self.rendered
