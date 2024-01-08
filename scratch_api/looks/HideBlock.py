from ..block import Block


class HideBlock(Block):
    def execute(self) -> bool:
        self.sprite.hide()
        
        return True
