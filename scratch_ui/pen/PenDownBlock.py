from ..block import Block
from ..template import Template

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.pen import PenDownBlock as PenDownGameBlock


class PenDownBlock(Block):
    game_block: PenDownGameBlock

    def init(self) -> None:
        self.template = Template([
            TextLineTemplateElement("pen down")
        ], (42, 174, 77))
