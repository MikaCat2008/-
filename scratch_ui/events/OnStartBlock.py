from ..block import Block
from ..template import Template
from ..block_slot import BlockSlot

from ..template_elements.TextTemplateElement import TextTemplateElement
from ..template_elements.BlocksTemplateElement import BlocksTemplateElement

from scratch_api.events import OnStartBlock as OnStartGameBlock


class OnStartBlock(Block):
    game_block: OnStartGameBlock

    def init(self) -> None:
        self.slots = [
            BlockSlot(self.game_block.blocks, self)
        ]

        self.template = Template([
            TextTemplateElement(
                "when Start clicked"
            ),
            BlocksTemplateElement(
                slot = self.slots[0],
                indent = False
            )
        ], (255, 100, 0))
