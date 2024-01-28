from ..nodes.NumberNode import NumberNode
from ..template import Template
from ..template_elements import TextTemplateElement

from scratch_api.motion import DirectionNode as DirectionGameNode


class DirectionNode(NumberNode):
    game_node: DirectionGameNode

    def init(self) -> None:
        self.template = Template([
            TextTemplateElement("direction")
        ], (0, 0, 255), "node")
