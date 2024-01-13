from pygame.event import EventType
from pygame.surface import SurfaceType

from .abstractions import FrameType


class Frame(FrameType):
    def __init__(
        self, 
        screen: SurfaceType,
        size: tuple[int, int],
        coords: tuple[int, int],
    ) -> None:
        self.screen = screen.subsurface(coords, size)
        self.size = size
        self.coords = coords
        self.frames = []

    def start(self) -> None:
        ...

    def start_frames(self) -> None:
        for frame in self.frames:
            frame.start()
            frame.start_frames()

    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        ...

    def update_frames(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        for frame in self.frames:
            mx, my = mouse_coords[0] - frame.coords[0], mouse_coords[1] - frame.coords[1]
            
            frame.update_frames(events, (mx, my))
            frame.update(events, (mx, my))
