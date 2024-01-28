from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import SetYToBlock as SetYToGameBlock


class SetYToBlock(Block):
    game_block: SetYToGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.y)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "set y to <0>", 
                self.slots[0]
            )
        ], (0, 0, 255))
