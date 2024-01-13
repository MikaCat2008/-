from pygame.draw import line, rect
from pygame.event import EventType

from ..frame import Frame
from .FieldFrame import FieldFrame
from .BlocksFrame import BlocksFrame


class ScriptsFrame(Frame):
    def start(self) -> None:
        self.frames = [
            FieldFrame(self.screen, (569, 730), (201, 0)),
            BlocksFrame(self.screen, (200, 730), (0, 0))
        ]

    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        line(self.screen, (180, 180, 180), (200, 0), (200, 730))
        rect(self.screen, (180, 180, 180), (0, 0, *self.screen.get_size()), 1)
