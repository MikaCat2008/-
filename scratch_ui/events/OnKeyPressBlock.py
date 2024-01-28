from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot
from ..block_slot import BlockSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement
from ..template_elements.BlocksTemplateElement import BlocksTemplateElement

from scratch_api.events import OnKeyPressBlock as OnKeyPressGameBlock


class OnKeyPressBlock(Block):
    game_block: OnKeyPressGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.key),
            BlockSlot(self.game_block.blocks)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "when <0> key pressed",
                self.slots[0]
            ),
            BlocksTemplateElement(
                slot = self.slots[1],
                indent = False
            )
        ], (174, 64, 0))
