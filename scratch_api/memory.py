from pygame.surface import SurfaceType

from .abstractions import SpriteType


class Memory:
    screen: SurfaceType
    sprites: list[SpriteType]

    def __init__(self) -> None:
        self.screen = None
        self.sprites = []


memory = Memory()
