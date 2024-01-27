from pygame.surface import SurfaceType

from .abstractions import GameNodeType, NodeSlotType
from .node import Node


class NodeSlot(NodeSlotType):
    def __init__(self, game_node: GameNodeType) -> None:
        self.node = Node.node_manager.create_node(game_node)

    def render(self) -> SurfaceType:
        return self.node.render()
