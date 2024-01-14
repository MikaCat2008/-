from pygame import mouse
from pygame.draw import rect
from pygame.event import EventType
from pygame.surface import SurfaceType

from ..abstractions import SpriteType
from ..frame import Frame
from ..block_manager import block_manager
from ..sprite_manager import sprite_manager


def update_blocks_field(screen: SurfaceType, selected_sprite: SpriteType, mx: int, my: int) -> None:
    m0 = mouse.get_pressed()[0]

    hovered_block = None
    for block in selected_sprite.blocks:
        x, y = block.coords
        w, h = block.rendered.get_size()
        
        if x <= mx <= x + w and y <= my <= y + h:
            child, cx, cy = block.get_child(mx - x, my - y)
            
            if child:
                hovered_block = child
                cw, ch = child.rendered.get_size()

                if block_manager.selected_block:
                    slot, slot_w, slot_y = hovered_block.get_slot_by_coords(mx - x - cx, my - y - cy)

                    if slot:
                        rect(screen, (0, 0, 0), (x + cx + 20, y + cy + slot_y - 15, slot_w, 15), 1)
                else:
                    rect(screen, (0, 0, 0), (x + cx, y + cy, cw, ch), 1)

                if m0 and not block_manager.selected_block:
                    block_manager.select(child)
                    block_manager.free()

            break

    block = block_manager.selected_block

    if block:
        bx, by, bw, bh = block.rendered.get_rect()

        if not m0:
            block_manager.unselect()
            
            if block.is_event():
                return 

            if hovered_block:
                if hovered_block.is_iterable():
                    if slot:
                        slot.add(block)
                    else:
                        if hovered_block.is_event():
                            hovered_block.slots[-1].add(block)
                        else:
                            hovered_block.slot.add(block)
                else:
                    hovered_block.slot.add(block)
        else:
            block.coords = mx - bw / 2, my - 10


def draw_blocks_field(screen: SurfaceType, sprite: SpriteType) -> None:
    for block in sprite.blocks:
        screen.blit(block.render(), block.coords)

    block = block_manager.selected_block
    
    if block:
        screen.blit(block.render(), block.coords)


class FieldFrame(Frame):
    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        self.screen.fill((255, 255, 255))

        if sprite_manager.selected_sprite:
            draw_blocks_field(self.screen, sprite_manager.selected_sprite)

            update_blocks_field(self.screen, sprite_manager.selected_sprite, *mouse_coords)
