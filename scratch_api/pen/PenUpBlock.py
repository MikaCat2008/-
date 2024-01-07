from ..block import Block


class PenUpBlock(Block):
    def execute(self) -> bool:
        self.sprite.pen.up()
        
        return True
