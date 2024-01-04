from ..abstractions import String, NodeType
from ..block import Block
from ..nodes.NumberNode import NumberNode


class ChangeValueByBlock(Block):
    name: String
    value: NodeType

    def __init__(self, *args: tuple[String, NodeType]) -> None:
        super().__init__(args)

        self.name = args[0]
        self.value = args[1]

    def execute(self) -> bool:
        name = str(self.name)
        value = self.value.get_value()

        self.sprite.set_value(
            name, 
            self.ctx(NumberNode(self.sprite.get_value(name) + value))
        )

        return True
