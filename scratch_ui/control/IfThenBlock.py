from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot
from ..block_slot import BlockSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement
from ..template_elements.BlocksTemplateElement import BlocksTemplateElement
from ..template_elements.BlocksBottomTemplateElement import BlocksBottomTemplateElement

from scratch_api.control import IfThenBlock as IfThenGameBlock


class IfThenBlock(Block):
    game_block: IfThenGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.condition),
            BlockSlot(self.game_block.blocks)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "if <0> then",
                self.slots[0]
            ),
            BlocksTemplateElement(
                slot = self.slots[1],
                indent = True
            ),
            BlocksBottomTemplateElement()
        ], (255, 145, 0))