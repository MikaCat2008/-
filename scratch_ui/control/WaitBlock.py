from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.control import WaitBlock as WaitGameBlock


class WaitBlock(Block):
    game_block: WaitGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.freeze_time)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "wait <0> secs", 
                self.slots[0]
            )
        ], (255, 145, 0))