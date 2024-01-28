from .abstractions import InputManagerType


class InputManager(InputManagerType):    
    def __init__(self) -> None:
        self.key_map = {}
        self.key_pmap = {}

    def update(self, state: bool, scancode: int) -> None:
        if 4 <= scancode <= 29:
            symbol = chr(scancode + 61).casefold()
        elif 30 <= scancode <= 39:
            if 30 <= scancode <= 38:
                symbol = str(scancode - 29)
            else:
                symbol = "0"
        elif scancode == 41:
            symbol = "esc"
        elif scancode == 44:
            symbol = "space"
        elif scancode == 42:
            symbol = "backspace"
        elif scancode == 45:
            symbol = "-"
        elif scancode == 55:
            symbol = "."
        else:
            symbol = ""
            
        if state and not self.key_map.get(symbol):
            self.key_pmap[symbol] = True

        self.key_map[symbol] = state


input_manager = InputManager()
