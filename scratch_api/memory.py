from .abstractions import MemoryType


class Memory(MemoryType):
    def __init__(self) -> None:
        self.screen = None
        self.stamp_screen = None
        self.sprites = []
        self.mouse_pos = (0, 0)


memory = Memory()
