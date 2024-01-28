from ..block import Block
from ..template import Template
from ..block_slot import BlockSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement
from ..template_elements.BlocksTemplateElement import BlocksTemplateElement
from ..template_elements.BlocksBottomTemplateElement import BlocksBottomTemplateElement

from scratch_api.control import ForeverBlock as ForeverGameBlock


class ForeverBlock(Block):
    game_block: ForeverGameBlock

    def init(self) -> None:
        self.slots = [
            BlockSlot(self.game_block.blocks)
        ]

        self.template = Template([
            TextLineTemplateElement("forever"),
            BlocksTemplateElement(
                slot = self.slots[0],
                indent = True
            ),
            BlocksBottomTemplateElement()
        ], (255, 145, 0))