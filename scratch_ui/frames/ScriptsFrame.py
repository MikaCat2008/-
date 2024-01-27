from pygame.draw import line, rect
from pygame.event import EventType

from ..frame import Frame
from .FieldFrame import FieldFrame
from .BlocksFrame import BlocksFrame


class ScriptsFrame(Frame):
    def start(self) -> None:
        self.frames = [
            FieldFrame(self.screen, (538, 730), (232, 0)),
            BlocksFrame(self.screen, (231, 730), (0, 0))
        ]

    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        line(self.screen, (180, 180, 180), (231, 0), (231, 730))
        rect(self.screen, (180, 180, 180), (0, 0, *self.screen.get_size()), 1)
