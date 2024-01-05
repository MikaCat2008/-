from __future__ import annotations

import pygame
from pygame.event import EventType
from pygame.transform import flip, rotate
from pygame.display import flip as flip_screen
from pygame.surface import SurfaceType

from .abstractions import SpriteType
from .emit import emit
from .memory import memory

screen: SurfaceType = None
key_map: dict[str, bool] = {}

__api_version__ = 0, 0


def set_screen(_screen: SurfaceType) -> None:
    global screen

    screen = _screen


def set_sprites(sprites: list[SpriteType]) -> None:
    memory.sprites = sprites


def start() -> None:
    emit("start")


def update(events: list[EventType]) -> None:
    screen.fill((255, 255, 255))

    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
            state = event.type == pygame.KEYDOWN

            if 4 <= event.scancode <= 29:
                symbol = chr(event.scancode + 61).casefold()

                key_map[symbol] = state
            elif event.scancode == 44:
                key_map["space"] = state
            elif 30 <= event.scancode <= 39:
                if 30 <= event.scancode <= 38:
                    symbol = str(event.scancode - 29)
                else:
                    symbol = "0"
                
                key_map[symbol] = state

    any_key = False

    for key, _ in filter(lambda x: x[1], key_map.items()):
        any_key = True
        
        emit("key", key=key)

    if any_key:
        emit("key", key="any")
    
    for sprite in memory.sprites:
        sprite.update()

    for sprite in memory.sprites:
        x, y = sprite.coords

        if sprite.rotate_style == 1:
            surface = rotate(sprite.surface, sprite.direction)
        elif sprite.rotate_style == 2:
            surface = sprite.surface
            direction = sprite.direction

            if 90 < direction < 270:
                surface = flip(surface, False, True)

            surface = rotate(surface, direction)

        w, h = surface.get_size()

        sprite.display_coords = (x - w / 2, y - h / 2)

        screen.blit(surface, sprite.display_coords)

    flip_screen()
