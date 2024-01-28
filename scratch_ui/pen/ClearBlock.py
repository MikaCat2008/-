from ..block import Block
from ..template import Template

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.pen import ClearBlock as ClearGameBlock


class ClearBlock(Block):
    game_block: ClearGameBlock

    def init(self) -> None:
        self.template = Template([
            TextLineTemplateElement("clear")
        ], (42, 174, 77))
