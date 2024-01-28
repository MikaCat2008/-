from ..block import Block
from ..template import Template

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.pen import StampBlock as StampGameBlock


class StampBlock(Block):
    game_block: StampGameBlock

    def init(self) -> None:
        self.template = Template([
            TextLineTemplateElement("stamp")
        ], (42, 174, 77))
