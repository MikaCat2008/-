from pygame.surface import SurfaceType

from .abstractions import (
    NodeType, NodeSlotType, GameNodeType, NodeManagerType
)
from scratch_api.nodes import NumberNode as NumberGameNode


class Node(NodeType):
    def __init__(self, game_node: GameNodeType) -> None:
        super().__init__()

        self.game_node = game_node
        self.nodes = []
        self.coords = None
        self.rendered = None
        self.slot = None
        self.template = None

        self.parent_node = None
        self.parent_block = None

        self.init()

        for node_slot in self.nodes:
            node_slot.node.parent_node = self
            node_slot.node.game_node.parent_node = game_node

    def init(self) -> None:
        ...

    def get_child(self, mx: int) -> tuple[NodeType, int]:
        for node_slot in self.nodes:
            node = node_slot.node

            nx = node.coords[0]
            nw = node.rendered.get_width()

            if nx <= mx <= nx + nw:
                child, cx = node.get_child(mx - nx)
                
                return child, cx + nx

        return self, 0

    def render(self) -> SurfaceType:
        self.rendered = self.template.render()
        
        return self.rendered
    
    def remove(self) -> None:
        if self.slot:
            self.slot.set_node(self.up(NumberGameNode(0)).node)

    def up(self, game_node: GameNodeType) -> NodeSlotType:
        node_slot = self.node_manager.create_slot(game_node)

        node_slot.parent_node = self
        node_slot.node.parent_node = self
        
        return node_slot

    @classmethod
    def set_node_manager(cls, node_manager: NodeManagerType) -> None:
        cls.node_manager = node_manager
