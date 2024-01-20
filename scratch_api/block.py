from time import time

from .abstractions import BlockType, NodeType, SpriteType
from .memory import memory


def StructureBlock[BlockType](cls: type[BlockType]) -> type[BlockType]:
    cls.is_structure = True
    
    return cls


class Block(BlockType):
    event = None
    is_structure = False

    def __init__(self) -> None:
        super().__init__()

        self.main_block = None
        self.parent_block = None
        self.parent_blocks = None
        self.sprite = None
        self.unfreeze_time = 0

        self.nodes = []

    def execute(self, **data: dict[str, object]) -> bool:
        ...

    def next(self) -> BlockType | None:
        ...

    def again(self) -> None:
        ...

    def freeze(self, seconds: float) -> None:
        self.unfreeze_time = max(time() + seconds, self.unfreeze_time)

    def init_nodes(self) -> None:
        self.nodes = [node for _, node in self.__dict__.items() if isinstance(node, NodeType)]

        for node in self.nodes:
            node.init(self.sprite)

    def reset_nodes(self) -> None:
        for node in self.nodes:
            node.reset()

    def is_freeze(self) -> bool:
        return self.unfreeze_time > time()

    def stop(self) -> None:
        ...

    def remove(self) -> None:
        if self.parent_blocks:
            self.parent_blocks.remove(self)
        elif self in self.sprite.blocks:
            self.sprite.blocks.remove(self)

    def get_sprite_by_name(self, name: str) -> SpriteType:
        return [sprite for sprite in memory.sprites if sprite.name == name][0]
