from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import PointTowardsBlock as PointTowardsGameBlock


class PointTowardsBlock(Block):
    game_block: PointTowardsGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.sprite_name),
            NodeSlot(self.game_block.mouse_pointer)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "point towards <0> mouse: <1>", 
                *self.slots
            )
        ], (0, 0, 255))
