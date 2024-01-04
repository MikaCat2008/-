from .abstractions import SpriteType


class Memory:
    sprites: list[SpriteType]

    def __init__(self) -> None:
        self.sprites = []


memory = Memory()
