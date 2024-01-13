from ..node import Node

from scratch_api.abstractions import BooleanNodeType as BooleanGameNodeType


class BooleanNode(Node):
    game_node: BooleanGameNodeType

    def get_str(self) -> str:
        return "true" if self.game_node.get_value() else "false"
