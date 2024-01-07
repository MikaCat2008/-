from pygame.surface import SurfaceType

from .memory import memory


def clear() -> None:
    memory.stamp_screen.fill((255, 255, 255, 255))


def stamp(surface: SurfaceType, coords: tuple[int, int]) -> None:
    memory.stamp_screen.blit(surface, coords)
