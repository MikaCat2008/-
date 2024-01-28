from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot
from ..block_slot import BlockSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement
from ..template_elements.BlocksTemplateElement import BlocksTemplateElement
from ..template_elements.BlocksBottomTemplateElement import BlocksBottomTemplateElement

from scratch_api.control import RepeatUntilBlock as RepeatUntilGameBlock


class RepeatUntilBlock(Block):
    game_block: RepeatUntilGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.condition),
            BlockSlot(self.game_block.blocks)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "repeat until <0>",
                self.slots[0]
            ),
            BlocksTemplateElement(
                slot = self.slots[1],
                indent = True
            ),
            BlocksBottomTemplateElement()
        ], (255, 145, 0))