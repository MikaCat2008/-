from ..node import Node

from scratch_api.abstractions import StringNodeType as StringGameNodeType


class StringNode(Node):
    game_node: StringGameNodeType

    def get_str(self) -> str:
        return f"\"{self.game_node.get_value()}\""
