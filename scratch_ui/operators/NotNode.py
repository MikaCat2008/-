from ..nodes.NumberNode import NumberNode
from ..template import Template
from ..template_elements import TextTemplateElement

from scratch_api.operators import NotNode as NotGameNode


class NotNode(NumberNode):
    game_node: NotGameNode

    def init(self) -> None:
        self.nodes = [
            self.up(self.game_node.value)
        ]

        self.template = Template([
            TextTemplateElement(
                "not <0>", 
                *self.nodes,
                color = (0, 0, 0)
            )
        ], (0, 255, 0), "node")
