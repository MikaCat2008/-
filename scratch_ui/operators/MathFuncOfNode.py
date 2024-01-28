from ..nodes.NumberNode import NumberNode
from ..template import Template
from ..template_elements import TextTemplateElement

from scratch_api.operators import MathFuncOfNode as MathFuncOfNodeGameNode


class MathFuncOfNode(NumberNode):
    game_node: MathFuncOfNodeGameNode

    def init(self) -> None:
        self.nodes = [
            self.up(self.game_node.func),
            self.up(self.game_node.number)
        ]

        self.template = Template([
            TextTemplateElement(
                "<0> of <1>", 
                *self.nodes,
                color = (0, 0, 0)
            )
        ], (0, 255, 0), "node")
