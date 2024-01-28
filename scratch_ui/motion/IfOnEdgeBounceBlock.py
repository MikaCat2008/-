from ..block import Block
from ..template import Template

from ..template_elements.TextLineTemplateElement import TextLineTemplateElement

from scratch_api.motion import IfOnEdgeBounceBlock as IfOnEdgeBounceGameBlock


class IfOnEdgeBounceBlock(Block):
    game_block: IfOnEdgeBounceGameBlock

    def init(self) -> None:
        self.template = Template([
            TextLineTemplateElement("if on edge, bounce")
        ], (0, 0, 255))
