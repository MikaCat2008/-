from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.data import SetValueToBlock as SetValueToGameBlock


class SetValueToBlock(Block):
    game_block: SetValueToGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.name),
            NodeSlot(self.game_block.value)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "set <0> to <1>", 
                *self.slots
            )
        ], (255, 94, 0))
