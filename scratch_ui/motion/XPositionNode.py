from ..nodes.NumberNode import NumberNode
from ..template import Template
from ..template_elements import TextTemplateElement

from scratch_api.motion import XPositionNode as XPositionGameNode


class XPositionNode(NumberNode):
    game_node: XPositionGameNode

    def init(self) -> None:
        self.template = Template([
            TextTemplateElement("x position")
        ], (0, 0, 255), "node")
