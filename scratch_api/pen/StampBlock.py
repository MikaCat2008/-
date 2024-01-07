from ..block import Block


class StampBlock(Block):
    def execute(self) -> bool:
        self.sprite.stamp()

        return True
