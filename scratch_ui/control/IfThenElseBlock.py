from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot
from ..block_slot import BlockSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement
from ..template_elements.BlocksTemplateElement import BlocksTemplateElement
from ..template_elements.BlocksBottomTemplateElement import BlocksBottomTemplateElement

from scratch_api.control import IfThenElseBlock as IfThenElseGameBlock


class IfThenElseBlock(Block):
    game_block: IfThenElseGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.condition),
            BlockSlot(self.game_block.then_blocks),
            BlockSlot(self.game_block.else_blocks)
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
            TextLineTemplateElement("else"),
            BlocksTemplateElement(
                slot = self.slots[2],
                indent = True
            ),
            BlocksBottomTemplateElement()
        ], (255, 145, 0))