from ..node import Node

from scratch_api.abstractions import StringNodeType as StringGameNodeType


class StringNode(Node):
    game_node: StringGameNodeType
