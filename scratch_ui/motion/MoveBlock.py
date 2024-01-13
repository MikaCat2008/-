from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextTemplateElement import TextTemplateElement

from scratch_api.motion import MoveBlock as MoveGameBlock


class MoveBlock(Block):
    game_block: MoveGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.velocity)
        ]

        self.template = Template([
            TextTemplateElement(
                "move <0> steps", 
                self.slots[0]
            )
        ], (0, 0, 255))
