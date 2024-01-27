import pygame
from pygame import mouse
from pygame.event import EventType
from pygame.surface import SurfaceType

from ..abstractions import BlockType, GameBlockType, GameObjectType, SpawnerType
from ..frame import Frame
from ..node_spawner import NodeSpawner
from ..block_spawner import BlockSpawner
from ..select_manager import select_manager

from scratch_api.nodes import NumberNode

from scratch_api.motion import MoveBlock

from scratch_api.events import OnStartBlock

from scratch_api.control import RepeatBlock

from scratch_api.operators import AddNode
from scratch_api.operators import SubNode
from scratch_api.operators import MulNode
from scratch_api.operators import DivNode


def get_spawners(
    *game_object_groups: tuple[tuple[tuple[GameObjectType], ...], tuple[int, int]]
) -> list[BlockType]:
    spawners = [None] * sum(map(len, game_object_groups))
    
    i, y = 0, 10
    for game_blocks in game_object_groups:
        for game_object in game_blocks:
            if isinstance(game_object, GameBlockType):
                spawner = BlockSpawner(
                    (10, y),
                    game_object
                )
            else:
                spawner = NodeSpawner(
                    (10, y),
                    game_object
                )

            spawners[i] = spawner
            
            i += 1
            y += 5 + spawner.render().get_height()
        y += 20
    
    return spawners


def update_spawners(spawners: list[SpawnerType], mx: int, my: int) -> None:
    m0 = mouse.get_pressed()[0]

    for spawner in spawners:
        x, y = spawner.coords
        w, h = spawner.render().get_size()
        
        if x <= mx <= x + w and y <= my <= y + h:
            if m0 and not select_manager.selected_object:
                select_manager.select(spawner.spawn())
                select_manager.free()

            break


def draw_spawners(screen: SurfaceType, scroll: int) -> None:
    for spawner in spawners:
        bx, by = spawner.coords

        screen.blit(spawner.render(), (bx, by - scroll))


spawners = None


class BlocksFrame(Frame):
    def start(self) -> None:
        global spawners

        self.scroll = 0

        spawners = get_spawners(
            (
                MoveBlock(NumberNode(10)),
            ),
            (
                OnStartBlock([]),
            ),
            (
                RepeatBlock(NumberNode(5), []),
            ),
            (
                AddNode(NumberNode(0), NumberNode(0)),
                SubNode(NumberNode(0), NumberNode(0)),
                MulNode(NumberNode(0), NumberNode(0)),
                DivNode(NumberNode(0), NumberNode(1))
            )
        )

    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        self.screen.fill((255, 255, 255))

        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                self.scroll = min(max(self.scroll - event.y * 25, 0), self.screen.get_height())

        draw_spawners(self.screen, self.scroll)

        mx, my = mouse_coords
        update_spawners(spawners, mx, my + self.scroll)
