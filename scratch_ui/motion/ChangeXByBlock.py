from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import ChangeXByBlock as ChangeXByGameBlock


class ChangeXByBlock(Block):
    game_block: ChangeXByGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.x)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "change x by <0>", 
                *self.slots
            )
        ], (0, 0, 255))
