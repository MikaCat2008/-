from .abstractions import NodeType, InputFieldType, InputManagerType
from .nodes import NumberNode, StringNode, BooleanNode

from scratch_api.input_manager import input_manager as game_input_manager


class NumberInputField(InputFieldType):
    node: NumberNode

    def __init__(self, node: NumberNode) -> None:
        self.node = node

    def press(self, key: str) -> None:
        value = self.node.game_node.value
        new_value = None

        if key == "backspace":
            if value < 10:
                new_value = 0
            else:
                new_value = int(str(value)[:-1])
        elif len(key) == 1 and 48 <= ord(key) <= 57:
            v = str(value) + key
            
            new_value = float(v) if "." in v else int(v)
        elif key == "-":
            new_value = -value

        if new_value is not None:
            self.node.game_node.value = new_value


class StringInputField(InputFieldType):
    noed: StringNode

    def __init__(self, node: StringNode) -> None:
        self.node = node

    def press(self, key: str) -> None:
        value = self.node.game_node.value
        new_value = None
        
        if key == "backspace" and len(key):
            new_value = value[:-1]
        elif key.isprintable():
            new_value = value + key

        if new_value is not None:
            self.node.game_node.value = new_value


class BooleanInputField(InputFieldType):
    node: BooleanNode

    def __init__(self, node: BooleanNode) -> None:
        self.node = node

    def press(self, key: str) -> None:
        new_value = None
        
        if key == "0":
            new_value = False
        elif key == "1":
            new_value = True

        if new_value is not None:
            self.node.game_node.value = new_value


class InputManager(InputManagerType):
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
        elif isinstance(selectable, StringNode):
            self.selected_field = StringInputField(selectable)
        elif isinstance(selectable, BooleanNode):
            self.selected_field = BooleanInputField(selectable)


input_manager = InputManager()
