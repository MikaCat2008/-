from ..block import Block
from ..template import Template

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.looks import HideBlock as HideGameBlock


class HideBlock(Block):
    game_block: HideGameBlock

    def init(self) -> None:
        self.template = Template([
            TextLineTemplateElement("hide")
        ], (147, 0, 201))
