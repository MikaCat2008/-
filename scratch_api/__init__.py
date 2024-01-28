from __future__ import annotations

import pygame
from pygame.event import EventType
from pygame.transform import flip, rotate
from pygame.surface import Surface, SurfaceType

from .abstractions import SpriteType
from .emit import emit
from .memory import memory
from .input_manager import input_manager

__api_version__ = 1, 6


def set_screen(screen: SurfaceType) -> None:
    memory.screen = screen
    memory.stamp_screen = Surface(screen.get_size()).convert_alpha()

    memory.stamp_screen.fill((255, 255, 255, 255))


def set_sprites(sprites: list[SpriteType]) -> None:
    memory.sprites = sprites


def start() -> None:
    emit("start")


def stop() -> None:
    for sprite in memory.sprites:
        for block in sprite.blocks:
            block.stop()


def update(events: list[EventType], mouse_pos: tuple[int, int], keyboard: bool = True) -> None:
    memory.screen.fill((255, 255, 255))
    memory.mouse_pos = mouse_pos

    for key in input_manager.key_pmap:
        input_manager.key_pmap[key] = False

    for event in events:
        if event.type == pygame.QUIT:
            exit()
        
        elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
            input_manager.update(event.type == pygame.KEYDOWN, event.scancode)

    if keyboard:
        any_key = False
        
        for key, _ in filter(lambda x: x[1], input_manager.key_map.items()):
            any_key = True
            
            emit("key", key=key)

        if any_key:
            emit("key", key="any")
    
    changes = False
    for sprite in memory.sprites:
        if sprite.update():
            changes = True

    memory.screen.blit(memory.stamp_screen, (0, 0))

    for sprite in memory.sprites:
        x, y = sprite.coords

        if sprite.rotation_style == 1:
            surface = rotate(sprite.surface, sprite.direction)
        elif sprite.rotation_style == 2:
            surface = sprite.surface
            direction = sprite.direction

            if 90 < direction < 270:
                surface = flip(surface, False, True)

            surface = rotate(surface, direction)

        w, h = surface.get_size()

        sprite.rendered_coords = (x - w / 2, y - h / 2)
        sprite.rendered_surface = surface

        if sprite.is_show:
            memory.screen.blit(surface, sprite.rendered_coords)

    return changes
