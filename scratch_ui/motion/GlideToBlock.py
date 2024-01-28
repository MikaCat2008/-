from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import GlideToBlock as GlideToGameBlock


class GlideToBlock(Block):
    game_block: GlideToGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.seconds),
            NodeSlot(self.game_block.end_x),
            NodeSlot(self.game_block.end_y)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "glide <0> secs to x: <1> y: <2>", 
                *self.slots
            )
        ], (0, 0, 255))
