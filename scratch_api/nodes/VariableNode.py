from ..nodes.NumberNode import NumberNode
from ..nodes.StringNode import StringNode
from ..nodes.BooleanNode import BooleanNode


class VariableNode(NumberNode, StringNode, BooleanNode):
    name: str

    def __init__(self, name: str) -> None:
        super().__init__()

        self.name = name

    def get_value(self) -> object:
        return self.sprite.get_value(self.name)
