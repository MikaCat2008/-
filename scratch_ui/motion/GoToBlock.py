from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import GoToBlock as GoToGameBlock


class GoToBlock(Block):
    game_block: GoToGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.sprite_name),
            NodeSlot(self.game_block.mouse_pointer)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "go to <0> mouse: <1>", 
                *self.slots
            )
        ], (0, 0, 255))
