from ..node import Node

from scratch_api.abstractions import NumberNodeType as NumberGameNodeType


class NumberNode(Node):
    game_node: NumberGameNodeType

    def get_str(self) -> str:
        return f"{self.game_node.get_value()}"
