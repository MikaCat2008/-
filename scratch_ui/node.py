from .abstractions import NodeType, GameNodeType, NodeManagerType


class Node(NodeType):
    def __init__(self, game_node: GameNodeType) -> None:
        super().__init__()

        self.game_node = game_node
        self.nodes = []
        self.coords = None
        self.rendered = None

        self.init()

    def init(self) -> None:
        ...

    @classmethod
    def up(cls, game_node: GameNodeType) -> None:
        return cls.node_manager.create_node(game_node)

    @classmethod
    def set_node_manager(cls, node_manager: NodeManagerType) -> None:
        cls.node_manager = node_manager
