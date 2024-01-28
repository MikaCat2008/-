from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import SetXToBlock as SetXToGameBlock


class SetXToBlock(Block):
    game_block: SetXToGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.x)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "set x to <0>", 
                self.slots[0]
            )
        ], (0, 0, 255))
