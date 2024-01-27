from ..nodes.NumberNode import NumberNode
from ..template import Template
from ..template_elements import TextTemplateElement

from scratch_api.operators import DivNode as DivGameNode


class DivNode(NumberNode):
    game_node: DivGameNode

    def init(self) -> None:
        self.nodes = [
            self.up(self.game_node.a),
            self.up(self.game_node.b)
        ]

        self.template = Template([
            TextTemplateElement(
                "<0> / <1>", *self.nodes,
                color = (0, 0, 0)
            )
        ], (0, 255, 0), "node")
