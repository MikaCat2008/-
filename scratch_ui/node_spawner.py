from copy import deepcopy

from pygame.surface import SurfaceType

from .abstractions import NodeType, SpriteType, GameNodeType, NodeSpawnerType
from .node_manager import node_manager


class NodeSpawner(NodeSpawnerType):
    def __init__(self, coords: tuple[int, int], game_node: GameNodeType) -> None:
        self.coords = coords
        self.game_node = game_node

        self.node = self.spawn(None)

    def spawn(self, sprite: SpriteType) -> NodeType:
        node = node_manager.create_node(
            deepcopy(self.game_node)
        )
        
        if sprite:
            node.game_node.init(sprite.game_sprite)
        
        return node

    def render(self) -> SurfaceType:
        return self.node.render()
