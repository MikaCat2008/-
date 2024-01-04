from time import time
from functools import reduce

from scratch_api.abstractions import NodeType, Blocks, SpriteType
from .abstractions import BlockType


def StructureBlock[BlockType](cls: type[BlockType]) -> type[BlockType]:
    cls.is_structure = True
    
    return cls


class Block(BlockType):
    event = None
    is_structure = False

    def __init__(self, args: tuple) -> None:
        super().__init__()

        self.args = args
        self.unfreeze_time = 0

    def execute(self, **data: dict[str, object]) -> bool:
        ...

    def next(self) -> BlockType | None:
        ...

    def again(self) -> None:
        ...

    def get_all_nodes(self) -> list[NodeType]:
        return reduce(lambda x, y: x + [y], (arg for arg in self.args if isinstance(arg, NodeType)), [])

    def get_all_blocks(self) -> Blocks:
        return reduce(lambda x, y: x + y, (arg for arg in self.args if isinstance(arg, list)), [])

    def ctx(self, node: NodeType) -> NodeType:
        node.set_sprite(self.sprite)
        
        return node

    def set_sprite(self, sprite: SpriteType) -> None:
        for node in self.get_all_nodes():
            node.set_sprite(sprite)

        for block in self.get_all_blocks():
            block.set_sprite(sprite)

            block.sprite = sprite

        self.sprite = sprite

    def set_main(self, main_block: BlockType) -> None:
        for block in self.get_all_blocks():
            block.set_main(main_block)

            block.main_block = main_block

    def set_parent(self) -> None:
        for block in self.get_all_blocks():
            block.set_parent()

            block.parent_block = self

    def freeze(self, seconds: float) -> None:
        self.unfreeze_time = max(time() + seconds, self.unfreeze_time)

    def is_freeze(self) -> bool:
        return self.unfreeze_time > time()
