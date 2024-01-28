from ..nodes.NumberNode import NumberNode
from ..template import Template
from ..template_elements import TextTemplateElement

from scratch_api.motion import YPositionNode as YPositionGameNode


class YPositionNode(NumberNode):
    game_node: YPositionGameNode

    def init(self) -> None:
        self.template = Template([
            TextTemplateElement("y position")
        ], (0, 0, 255), "node")
