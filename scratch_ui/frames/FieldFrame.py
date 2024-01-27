from pygame import mouse
from pygame.draw import rect
from pygame.event import EventType
from pygame.surface import SurfaceType

from ..abstractions import SpriteType, NodeSlotType, BlockSlotType
from ..frame import Frame
from ..nodes import NumberNode
from ..block_manager import block_manager
from ..input_manager import input_manager
from ..select_manager import select_manager
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

                slot, slot_w, slot_y = hovered_block.get_slot_by_coords(mx - x - cx, my - y - cy)

                if slot:
                    block = select_manager.get_block()

                    if isinstance(slot, BlockSlotType) and block and not block.is_event:
                        rect(screen, (0, 0, 0), (x + cx + 20, y + cy + slot_y - 15, slot_w, 15), 1)
                    elif isinstance(slot, NodeSlotType):
                        cx = x + cx + slot_y + 4
                        child, _cx = slot.node.get_child(mx - cx)

                        rect(screen, (0, 0, 0), (cx + _cx, y + cy, child.rendered.get_width() + 1, 25), 1)
                else:
                    rect(screen, (0, 0, 0), (x + cx, y + cy, cw, ch), 1)

                if m0 and not select_manager.selected_object:
                    if isinstance(slot, NodeSlotType):
                        node = slot.node

                        if type(node) is NumberNode:
                            input_manager.select(node)
                        else:
                            select_manager.select(slot.node)
                            select_manager.free()
                    else:
                        select_manager.select(child)
                        select_manager.free()

            break

    selected_object = select_manager.selected_object

    if selected_object:
        node = select_manager.get_node()
        block = select_manager.get_block()

        if not m0:
            select_manager.unselect()

            if hovered_block:
                if block and not block.is_event():
                    if hovered_block.is_iterable():
                        if slot:
                            if isinstance(slot, BlockSlotType):
                                slot.add(block)
                        else:
                            if hovered_block.is_event():
                                hovered_block.slots[-1].add(block)
                            else:
                                if my - y - cy > hovered_block.rendered.get_height() / 2:
                                    hovered_block.slot.insert_after(hovered_block, block)
                                else:
                                    hovered_block.slot.insert_before(hovered_block, block)
                    else:
                        if my - y - cy > hovered_block.rendered.get_height() / 2:
                            hovered_block.slot.insert_after(hovered_block, block)
                        else:
                            hovered_block.slot.insert_before(hovered_block, block)
                elif node:
                    # print(node)
                    ...
            else:
                if block and block.is_event():
                    block.deep = 0
                    block.coords = mx - block.rendered.get_width() / 2, my - 10

                    selected_sprite.blocks.append(block)
                    selected_sprite.game_sprite.blocks.append(block.game_block)


def draw_blocks_field(screen: SurfaceType, sprite: SpriteType) -> None:
    for block in sprite.blocks:
        screen.blit(block.render(), block.coords)


class FieldFrame(Frame):
    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        self.screen.fill((255, 255, 255))

        if sprite_manager.selected_sprite:
            draw_blocks_field(self.screen, sprite_manager.selected_sprite)

            update_blocks_field(self.screen, sprite_manager.selected_sprite, *mouse_coords)
