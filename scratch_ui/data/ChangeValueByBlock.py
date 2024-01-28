from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.data import ChangeValueByBlock as ChangeValueByGameBlock


class ChangeValueByBlock(Block):
    game_block: ChangeValueByGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.name),
            NodeSlot(self.game_block.value)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "change <0> by <1>", 
                *self.slots
            )
        ], (255, 94, 0))
