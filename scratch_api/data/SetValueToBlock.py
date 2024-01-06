from ..abstractions import String, NodeType
from ..block import Block


class SetValueToBlock(Block):
    name: String
    value: NodeType

    def __init__(self, name: String, value: NodeType) -> None:
        super().__init__()

        self.name = name
        self.value = value

    def execute(self) -> bool:
        self.sprite.set_value(str(self.name), self.value)

        return True
