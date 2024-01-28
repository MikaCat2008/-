from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import GoToXYBlock as GoToXYGameBlock


class GoToXYBlock(Block):
    game_block: GoToXYGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.x),
            NodeSlot(self.game_block.y)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "go to x: <0> y: <1>", 
                *self.slots
            )
        ], (0, 0, 255))
