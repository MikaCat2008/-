from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import TurnLeftBlock as TurnLeftGameBlock


class TurnLeftBlock(Block):
    game_block: TurnLeftGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.angle)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "turn left <0> degrees", 
                *self.slots
            )
        ], (0, 0, 255))
