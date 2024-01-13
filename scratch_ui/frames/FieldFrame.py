from pygame.event import EventType
from pygame.surface import SurfaceType

from ..abstractions import SpriteType
from ..frame import Frame
from ..sprite_manager import sprite_manager


def draw_blocks_field(screen: SurfaceType, sprite: SpriteType) -> None:
    for block in sprite.blocks:
        screen.blit(block.render(), block.coords)


class FieldFrame(Frame):
    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        self.screen.fill((255, 255, 255))

        if sprite_manager.selected_sprite:
            draw_blocks_field(self.screen, sprite_manager.selected_sprite)
