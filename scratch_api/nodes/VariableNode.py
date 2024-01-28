from ..abstractions import String, VariableNodeType
from .NumberNode import NumberNode
from .StringNode import StringNode
from .BooleanNode import BooleanNode


class VariableNode(NumberNode, StringNode, BooleanNode, VariableNodeType):
    name: String

    def __init__(self, name: String) -> None:
        super().__init__(None)

        self.name = name

    def get_value(self) -> object:
        return self.sprite.get_value(str(self.name))
