from pygame.surface import SurfaceType

from .abstractions import NodeType, NodeSlotType, GameNodeType, NodeManagerType

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

        self.init()

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
        self.game_node.remove()
        
        if self.slot:
            node = self.slot.node
            new_node = self.up(NumberGameNode(0)).node
            slot = self.slot
            self.slot.node = new_node
            node.slot = None
            new_node.slot = slot
            self.slot = slot

            print(self.slot, new_node.slot)

    def up(self, game_node: GameNodeType) -> NodeSlotType:
        return self.node_manager.create_slot(game_node)

    @classmethod
    def set_node_manager(cls, node_manager: NodeManagerType) -> None:
        cls.node_manager = node_manager
