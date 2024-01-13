from pygame.surface import SurfaceType

from .abstractions import SpriteType


class Memory:
    screen: SurfaceType
    stamp_screen: SurfaceType
    sprites: list[SpriteType]
    mouse_pos: tuple[int, int]

    def __init__(self) -> None:
        self.screen = None
        self.stamp_screen = None
        self.sprites = []
        self.mouse_pos = (0, 0)


memory = Memory()
