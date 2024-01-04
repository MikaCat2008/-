from ..node import Node

from .NumberNode import NumberNode 
from .StringNode import StringNode
from .BooleanNode import BooleanNode 


class VariableNode(NumberNode, StringNode, BooleanNode, Node):
    name: str

    def __init__(self, name: str) -> None:
        super().__init__()

        self.name = name

    def get_value(self) -> object:
        return self.sprite.get_value(self.name)
