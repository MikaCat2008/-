from ..abstractions import String, Number
from ..block import Block
from ..nodes.NumberNode import NumberNode


class ChangeValueByBlock(Block):
    name: String
    value: Number

    def __init__(self, name: String, value: Number) -> None:
        super().__init__()

        self.name = name
        self.value = value

    def execute(self) -> bool:
        name = str(self.name)
        value = float(self.value)

        self.sprite.set_value(
            name, 
            NumberNode(self.sprite.get_value(name) + value)
        )

        return True
