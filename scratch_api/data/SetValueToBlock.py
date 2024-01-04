from ..abstractions import String, NodeType
from ..block import Block


class SetValueToBlock(Block):
    name: String
    value: NodeType

    def __init__(self, *args: tuple[String, NodeType]) -> None:
        super().__init__(args)

        self.name = args[0]
        self.value = args[1]

    def execute(self) -> bool:
        value = self.value.get_value()

        self.sprite.set_value(str(self.name), value)

        return True
