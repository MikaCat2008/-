from ..block import Block


class PenDownBlock(Block):
    def execute(self) -> bool:
        self.sprite.pen.down()
        
        return True
