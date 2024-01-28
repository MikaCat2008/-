from .abstractions import NodeType
from .nodes import NumberNode, BooleanNode

from scratch_api.input_manager import input_manager as game_input_manager


class InputField:
    def press(self, key: str) -> None:
        ...


class NumberInputField(InputField):
    def __init__(self, node: NumberNode) -> None:
        self.node = node

    def press(self, key: str) -> None:
        value = None

        if key == "backspace":
            value = self.node.game_node.value

            if value < 10:
                value = 0
            else:
                value = int(str(value)[:-1])
        elif len(key) == 1 and 48 <= ord(key) <= 57:
            value = int(str(self.node.game_node.value) + key)

        if value is not None:
            self.node.game_node.value = value


class BooleanInputField(InputField):
    def __init__(self, node: BooleanNode) -> None:
        self.node = node

    def press(self, key: str) -> None:
        value = None
        
        if key == "0":
            value = False
        elif key == "1":
            value = True

        if value is not None:
            self.node.game_node.value = value


class InputManager:
    selected_field: InputField

    def __init__(self) -> None:
        self.selected_field = None

    def update(self) -> None:
        if self.selected_field:
            for key in filter(lambda x: x[1], game_input_manager.key_pmap.items()):
                if key[0] == "esc":
                    self.selected_field = None

                    return

                self.selected_field.press(key[0])

    def select(self, selectable: NodeType) -> None:
        if isinstance(selectable, NumberNode):
            self.selected_field = NumberInputField(selectable)
        elif isinstance(selectable, BooleanNode):
            self.selected_field = BooleanInputField(selectable)


input_manager = InputManager()
