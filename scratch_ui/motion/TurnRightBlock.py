from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import TurnRightBlock as TurnRightGameBlock


class TurnRightBlock(Block):
    game_block: TurnRightGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.angle)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "turn right <0> degrees", 
                *self.slots
            )
        ], (0, 0, 255))
