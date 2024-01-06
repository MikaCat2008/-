from time import time
from functools import reduce

from .abstractions import BlockType, NodeType, Blocks, SpriteType
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
        self.sprite = None
        self.is_initialized = False
        self.unfreeze_time = 0

    def execute(self, **data: dict[str, object]) -> bool:
        ...

    def next(self) -> BlockType | None:
        ...

    def again(self) -> None:
        ...

    def freeze(self, seconds: float) -> None:
        self.unfreeze_time = max(time() + seconds, self.unfreeze_time)

    def init_nodes(self) -> None:
        for k, node in filter(lambda x: isinstance(x[1], NodeType), self.__dict__.items()):
            node.init(self.sprite)

    def is_freeze(self) -> bool:
        return self.unfreeze_time > time()

    def get_sprite_by_name(self, name: str) -> SpriteType:
        return [sprite for sprite in memory.sprites if sprite.name == name][0]
