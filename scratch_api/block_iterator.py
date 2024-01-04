from .abstractions import BlockType, Blocks
from .block import Block


class BlockIterator(Block):
    i: int
    __again: bool
    iter_blocks: Blocks

    def __init__(self, args: tuple) -> None:
        super().__init__(args)
        
        self.i = 0
        self.__again = False
        self.iter_blocks = []
    
    def iter(self) -> Blocks:
        return self.iter_blocks

    def next(self) -> BlockType | None:
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
            
            if isinstance(block, BlockIterator):
                if (next_block := block.next()):
                    return next_block 

            self.i += 1

            return block

        self.i = 0
        self.iter_blocks = self.iter()
        return None
    
    def again(self) -> None:
        self.__again = True
