from pygame.surface import SurfaceType

from ..abstractions import GameNodeType
from ..node import Node
from ..font import text_render

from scratch_api.abstractions import StringNodeType as StringGameNodeType


class StringNode(Node):
    game_node: StringGameNodeType

    def __init__(self, game_node: GameNodeType) -> None:
        super().__init__(game_node)

        self.prototype = StringNode

    def get_surfaces(self) -> list[SurfaceType]:
        return [self.render()]

    def render(self) -> SurfaceType:
        if self.template is None:
            self.rendered = text_render(self.game_node.get_value(), (0, 0, 0), (255, 255, 255), 3)
        else:
            self.rendered = self.template.render()

        self.check_selected()

        return self.rendered
