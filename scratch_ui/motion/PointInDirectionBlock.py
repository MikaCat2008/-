from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import PointInDirectionBlock as PointInDirectionGameBlock


class PointInDirectionBlock(Block):
    game_block: PointInDirectionGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.direction)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "point in direction <0>", 
                self.slots[0]
            )
        ], (0, 0, 255))
