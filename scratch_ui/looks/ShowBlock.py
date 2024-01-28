from ..block import Block
from ..template import Template

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.looks import ShowBlock as ShowGameBlock


class ShowBlock(Block):
    game_block: ShowGameBlock

    def init(self) -> None:
        self.template = Template([
            TextLineTemplateElement("show")
        ], (147, 0, 201))
