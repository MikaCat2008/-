from pygame.surface import SurfaceType

from ..abstractions import GameNodeType
from ..node import Node
from ..template import Template
from ..template_elements import TextTemplateElement

from scratch_api.abstractions import VariableNodeType as VariableGameNodeType


class VariableNode(Node):
    game_node: VariableGameNodeType

    def __init__(self, game_node: GameNodeType) -> None:
        super().__init__(game_node)

        self.prototype = VariableNode

    def init(self) -> None:
        self.nodes = [
            self.up(self.game_node.name)
        ]

        self.template = Template([
            TextTemplateElement(
                "  <0>", *self.nodes, indent = 2
            )
        ], (255, 0, 0), "node")

    def render(self) -> SurfaceType:
        self.rendered = self.template.render()
        
        self.check_selected()

        return self.rendered
