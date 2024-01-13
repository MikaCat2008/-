from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot
from ..block_slot import BlockSlot

from ..template_elements.TextTemplateElement import TextTemplateElement
from ..template_elements.BlocksTemplateElement import BlocksTemplateElement
from ..template_elements.BlocksBottomTemplateElement import BlocksBottomTemplateElement

from scratch_api.control import RepeatBlock as RepeatGameBlock


class RepeatBlock(Block):
    game_block: RepeatGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.end),
            BlockSlot(self.game_block.blocks, self)
        ]

        self.template = Template([
            TextTemplateElement(
                "repeat <0>",
                self.slots[0]
            ),
            BlocksTemplateElement(
                slot = self.slots[1],
                indent = True
            ),
            BlocksBottomTemplateElement()
        ], (255, 145, 0))