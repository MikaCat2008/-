from .abstractions import PenType, SpriteType
from .memory import memory


class Pen(PenType):
    def __init__(self, sprite: SpriteType, color: tuple[int, int, int], size: int) -> None:
        super().__init__()

        self.sprite = sprite
        self.color = color
        self.size = size
        self.is_down = False

    def stamp(self) -> None:
        memory.stamp_screen.blit(self.sprite.rendered_surface, self.sprite.rendered_coords)

    def down(self) -> None:
        self.is_down = True
    
    def up(self) -> None:
        self.is_down = False


def clear() -> None:
    memory.stamp_screen.fill((255, 255, 255, 255))

