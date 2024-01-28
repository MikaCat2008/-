from pygame.surface import SurfaceType

from ..abstractions import GameNodeType
from ..node import Node
from ..font import text_render

from scratch_api.abstractions import NumberNodeType as NumberGameNodeType


class NumberNode(Node):
    game_node: NumberGameNodeType

    def __init__(self, game_node: GameNodeType) -> None:
        super().__init__(game_node)

        self.prototype = NumberNode

    def get_surfaces(self) -> list[SurfaceType]:
        return [self.render()]

    def render(self) -> SurfaceType:
        if self.template is None:
            self.rendered = text_render(str(self.game_node.get_value()), (0, 0, 0), (255, 255, 255), 3)
        else:
            self.rendered = self.template.render()

        self.check_selected()

        return self.rendered
