from ..block import Block
from ..template import Template
from ..node_slot import NodeSlot

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import SetRotationStyleBlock as SetRotationStyleGameBlock


class SetRotationStyleBlock(Block):
    game_block: SetRotationStyleGameBlock

    def init(self) -> None:
        self.slots = [
            NodeSlot(self.game_block.rotation_style)
        ]

        self.template = Template([
            TextLineTemplateElement(
                "set rotation style <0>", 
                self.slots[0]
            )
        ], (0, 0, 255))
