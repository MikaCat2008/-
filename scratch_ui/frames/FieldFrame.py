from pygame import mouse
from pygame.draw import rect
from pygame.event import EventType
from pygame.surface import SurfaceType

from ..abstractions import SpriteType
from ..frame import Frame
from ..block_manager import block_manager
from ..sprite_manager import sprite_manager


def update_blocks_field(s, selected_sprite: SpriteType, mx: int, my: int) -> None:
    m0 = mouse.get_pressed()[0]

    if not block_manager.selected_block:
        for block in selected_sprite.blocks:
            x, y = block.coords
            w, h = block.rendered.get_size()
            
            if x <= mx <= x + w and y <= my <= y + h:
                child, cx, cy = block.get_child(mx - x, my - y)
                
                if child:
                    cw, ch = child.rendered.get_size()

                    rect(s, (0, 0, 0), (x + cx, y + cy, cw, ch), 1)

                break

    if block_manager.selected_block:
        x, y, w, h = block_manager.selected_block.rendered.get_rect()

        print(block_manager.selected_block)

        if not (m0 or x <= mx <= x + w and y <= my <= y + h):
            block_manager.selected_block = None
        else:
            block_manager.selected_block.coords = mx - w / 2, my - 10


def draw_blocks_field(screen: SurfaceType, sprite: SpriteType) -> None:
    for block in sprite.blocks:
        screen.blit(block.render(), block.coords)


class FieldFrame(Frame):
    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        self.screen.fill((255, 255, 255))

        if sprite_manager.selected_sprite:
            draw_blocks_field(self.screen, sprite_manager.selected_sprite)

            update_blocks_field(self.screen, sprite_manager.selected_sprite, *mouse_coords)
