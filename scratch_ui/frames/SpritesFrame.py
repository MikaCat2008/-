from pygame.draw import rect
from pygame.event import EventType

from ..frame import Frame


class SpritesFrame(Frame):
    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        self.screen.fill((255, 255, 255))

        rect(self.screen, (180, 180, 180), (0, 0, *self.screen.get_size()), 1)
