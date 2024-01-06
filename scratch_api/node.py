from .abstractions import NodeType, SpriteType


class Node(NodeType):
    def init(self, sprite: SpriteType) -> None:
        for _, node in filter(lambda x: isinstance(x[1], NodeType), self.__dict__.items()):
            node.init(sprite)
        
        self.sprite = sprite
