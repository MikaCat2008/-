from pygame.surface import SurfaceType

from .abstractions import GameNodeType, NodeSlotType
from .node import Node


class NodeSlot(NodeSlotType):
    def __init__(self, game_node: GameNodeType) -> None:
        node = Node.node_manager.create_node(game_node)
        self.node = node
        node.slot = self

    def render(self) -> SurfaceType:
        return self.node.render()
