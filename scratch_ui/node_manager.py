from .abstractions import NodeType, NodeManagerType
from .node import Node
from .nodes.NumberNode import NumberNode

from .operators.AddNode import AddNode

from scratch_api.abstractions import NodeType as GameNodeType
from scratch_api.nodes import NumberNode as NumberGameNode

from scratch_api.operators import AddNode as AddGameNode


class NodeManager(NodeManagerType):
    def create_node(
        self,
        game_node: GameNodeType
    ) -> NodeType:
        if isinstance(game_node, AddGameNode):
            node_factory = AddNode
        elif isinstance(game_node, NumberGameNode):
            node_factory = NumberNode

        return node_factory(game_node)


node_manager = NodeManager()
Node.set_node_manager(node_manager)
