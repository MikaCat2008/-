from ..abstractions import NodeType
from ..block import Block


class PrintBlock(Block):
    text: NodeType

    def __init__(self, *args: tuple[NodeType]) -> None:
        super().__init__(args)

        self.text = args[0]

    def execute(self) -> bool:
        print(self.text.get_value())

        return True
