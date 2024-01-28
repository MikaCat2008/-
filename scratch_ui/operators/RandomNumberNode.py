from ..nodes.NumberNode import NumberNode
from ..template import Template
from ..template_elements import TextTemplateElement

from scratch_api.operators import RandomNumberNode as RandomNumberGameNode


class RandomNumberNode(NumberNode):
    game_node: RandomNumberGameNode

    def init(self) -> None:
        self.nodes = [
            self.up(self.game_node.from_number),
            self.up(self.game_node.to_number)
        ]

        self.template = Template([
            TextTemplateElement(
                "pick random <0> to <1>", 
                *self.nodes,
                color = (0, 0, 0)
            )
        ], (0, 255, 0), "node")
