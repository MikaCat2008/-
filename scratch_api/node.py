from .abstractions import NodeType, SpriteType


class Node(NodeType):
    def set_sprite(self, sprite: SpriteType) -> None:
        for _, v in self.__dict__.items():
            if isinstance(v, NodeType):
                v.set_sprite(sprite)
        
        self.sprite = sprite
