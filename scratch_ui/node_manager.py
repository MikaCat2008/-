from .abstractions import NodeType, NodeSlotType, GameNodeType, NodeManagerType
from .node import Node
from .objects import objects
from .node_slot import NodeSlot


class NodeManager(NodeManagerType):
    def create_node(self, game_node: GameNodeType) -> NodeType:
        return objects[type(game_node)](game_node)
    
    def create_slot(self, game_node: GameNodeType) -> NodeSlotType:
        return NodeSlot(game_node)


node_manager = NodeManager()
Node.set_node_manager(node_manager)
