from pygame.event import EventType

from ..frame import Frame


class BlocksFrame(Frame):
    def start(self) -> None:
        ...

    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        self.screen.fill((255, 255, 255))
