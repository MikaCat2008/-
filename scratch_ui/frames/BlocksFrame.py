import pygame
from pygame import mouse
from pygame.draw import rect
from pygame.event import EventType
from pygame.surface import SurfaceType

from ..abstractions import BlockType, GameBlockType
from ..frame import Frame
from ..block_manager import block_manager
from ..block_spawner import BlockSpawner

from scratch_api.nodes import NumberNode

from scratch_api.motion import MoveBlock


def get_spawners(
    *game_block_groups: tuple[tuple[tuple[GameBlockType], ...], tuple[int, int]]
) -> list[BlockType]:
    block_spawners = [None] * sum(map(len, game_block_groups))
    
    i, y = 0, 10
    for game_blocks in game_block_groups:
        for game_block in game_blocks:
            block_spawner = BlockSpawner(
                (10, y),
                game_block
            )
            
            block_spawners[i] = block_spawner
            
            i += 1
            y += 5 + block_spawner.render().get_height()
        y += 20
    
    return block_spawners


def update_block_spawners(block_spawners: list[BlockType], mx: int, my: int) -> None:
    m0 = mouse.get_pressed()[0]

    for block_spawner in block_spawners:
        x, y = block_spawner.coords
        w, h = block_spawner.block.rendered.get_size()
        
        if x <= mx <= x + w and y <= my <= y + h:
            if m0 and not block_manager.selected_block:
                block = block_spawner.spawn()
                
                block_manager.select(block)
                block_manager.free()

            break


def draw_block_spawners(screen: SurfaceType, scroll: int) -> None:
    for block_spawner in block_spawners:
        bx, by = block_spawner.coords

        screen.blit(block_spawner.render(), (bx, by - scroll))


block_spawners = get_spawners(
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    ),
    (
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10)),
        MoveBlock(NumberNode(10))
    )
)


class BlocksFrame(Frame):
    def start(self) -> None:
        self.scroll = 0

    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        self.screen.fill((255, 255, 255))

        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                self.scroll -= event.y * 25

        draw_block_spawners(self.screen, self.scroll)

        mx, my = mouse_coords
        update_block_spawners(block_spawners, mx, my + self.scroll)
