from copy import deepcopy

from pygame.surface import SurfaceType

from .abstractions import NodeType, GameNodeType, NodeSpawnerType
from .node_manager import node_manager
from .sprite_manager import sprite_manager


class NodeSpawner(NodeSpawnerType):
    def __init__(self, coords: tuple[int, int], game_node: GameNodeType) -> None:
        self.coords = coords
        self.game_node = game_node

        self.node = self.spawn()

    def spawn(self) -> NodeType:
        return node_manager.create_node(
            deepcopy(self.game_node)
        )

    def render(self) -> SurfaceType:
        return self.node.render()
