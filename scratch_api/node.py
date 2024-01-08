from .abstractions import NodeType, SpriteType


class Node(NodeType):
    def __init__(self) -> None:
        super().__init__()

        self.nodes = []

    def init(self, sprite: SpriteType) -> None:
        self.nodes = [node for _, node in self.__dict__.items() if isinstance(node, NodeType)]
        
        for node in self.nodes:
            node.init(sprite)
        
        self.sprite = sprite

    def reset(self) -> None:
        for node in self.nodes:
            node.reset()
