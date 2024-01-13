from ..node import Node


class NumberNode(Node):
    def get_str(self) -> str:
        return f"({self.game_node.get_value()})"
