from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.control import WaitUntilBlock as WaitUntilGameBlock


class WaitUntilBlock(Block):
    game_block: WaitUntilGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.condition)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "wait until <0>", 
                self.slots[0]
            )
        ], (255, 145, 0))