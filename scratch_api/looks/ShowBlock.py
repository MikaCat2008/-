from ..block import Block


class ShowBlock(Block):
    def execute(self) -> bool:
        self.sprite.show()
        
        return True
