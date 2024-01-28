from pygame.surface import SurfaceType

from .abstractions import NodeType, GameNodeType, NodeSlotType
from .node import Node


class NodeSlot(NodeSlotType):
    def __init__(self, game_node: GameNodeType) -> None:
        node = Node.node_manager.create_node(game_node)
        self.node = node
        node.slot = self

        self.parent_node = None
        self.parent_block = None

    def set_node(self, node: NodeType) -> None:
        prev_node = self.node
        self.node = node
        node.slot = self
        node.game_node.sprite = prev_node.game_node.sprite

        if self.parent_node:
            node.parent_node = self.parent_node
            node.game_node.parent_node = self.parent_node.game_node

            self.parent_node.game_node.replace_node(prev_node.game_node, node.game_node)
        else:
            node.parent_node = None
            node.game_node.parent_node = None

            node.parent_block = self.parent_block
            node.game_node.parent_block = self.parent_block.game_block

            self.parent_block.game_block.replace_node(prev_node.game_node, node.game_node)

    def render(self) -> SurfaceType:
        return self.node.render()
