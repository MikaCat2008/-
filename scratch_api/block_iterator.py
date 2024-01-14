from .abstractions import BlockType, Blocks
from .block import Block, StructureBlock


@StructureBlock
class BlockIterator(Block):
    i: int
    __stop: bool
    __again: bool
    iter_blocks: Blocks

    def __init__(self, blocks: Blocks = None) -> None:
        super().__init__()
        
        self.i = 0
        self.__stop = False
        self.__again = False
        self.iter_blocks = blocks or []
    
    def execute(self) -> bool:
        return True

    def iter(self) -> Blocks:
        return self.iter_blocks

    def next(self) -> BlockType | None:
        if self.__stop:
            self.__stop = False

            return None

        if self.__again:
            block = self.iter_blocks[self.i - 1]

            if isinstance(block, BlockIterator):
                if (next_block := block.next()):
                    return next_block 

            self.__again = False

            return block

        if not self.iter_blocks:
            self.iter_blocks = self.iter()

        if self.i < len(self.iter_blocks):
            block = self.iter_blocks[self.i]

            if block.parent_block is None:
                block.parent_block = self

            if isinstance(block, BlockIterator):
                if block.sprite is None:
                    block.sprite = self.sprite

                    block.init_nodes()

                if (next_block := block.next()):
                    return next_block

            self.i += 1

            return block

        self.i = 0
        self.iter_blocks = self.iter()

        return None
    
    def again(self) -> None:
        self.__again = True

    def stop(self) -> None:
        self.i = 0
        self.__again = False
        self.__stop = True

        for block in self.iter_blocks:
            block.stop()

        self.iter_blocks = []
