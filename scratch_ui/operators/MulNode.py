from ..nodes.NumberNode import NumberNode

from scratch_api.operators import MulNode as MulGameNode


class MulNode(NumberNode):
    game_node: MulGameNode

    def init(self) -> None:
        self.nodes = [
            self.up(self.game_node.a),
            self.up(self.game_node.b)
        ]
    
    def get_str(self) -> str:
        return f"({self.nodes[0].get_str()} * {self.nodes[1].get_str()})"
