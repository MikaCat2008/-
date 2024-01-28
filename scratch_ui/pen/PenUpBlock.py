from ..block import Block
from ..template import Template

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.pen import PenUpBlock as PenUpGameBlock


class PenUpBlock(Block):
    game_block: PenUpGameBlock

    def init(self) -> None:
        self.template = Template([
            TextLineTemplateElement("pen up")
        ], (42, 174, 77))
