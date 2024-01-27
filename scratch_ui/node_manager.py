from .abstractions import NodeType, NodeSlotType, NodeManagerType
from .node import Node
from .node_slot import NodeSlot

from .nodes import NumberNode

from .operators import AddNode
from .operators import SubNode
from .operators import MulNode
from .operators import DivNode

from scratch_api.abstractions import NodeType as GameNodeType

from scratch_api.nodes import NumberNode as NumberGameNode

from scratch_api.operators import AddNode as AddGameNode
from scratch_api.operators import SubNode as SubGameNode
from scratch_api.operators import MulNode as MulGameNode
from scratch_api.operators import DivNode as DivGameNode


class NodeManager(NodeManagerType):
    def create_node(self, game_node: GameNodeType) -> NodeType:
        if isinstance(game_node, AddGameNode):
            node_factory = AddNode
        elif isinstance(game_node, SubGameNode):
            node_factory = SubNode
        elif isinstance(game_node, MulGameNode):
            node_factory = MulNode
        elif isinstance(game_node, DivGameNode):
            node_factory = DivNode
        elif isinstance(game_node, NumberGameNode):
            node_factory = NumberNode

        return node_factory(game_node)
    
    def create_slot(self, game_node: GameNodeType) -> NodeSlotType:
        return NodeSlot(game_node)


node_manager = NodeManager()
Node.set_node_manager(node_manager)
