from pygame.draw import rect
from pygame.event import EventType

from ..frame import Frame

from scratch_api import set_screen, update as update_game


class GameFrame(Frame):    
    def start(self) -> None:
        set_screen(self.screen)
    
    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        update_game(events, mouse_coords)

        rect(self.screen, (180, 180, 180), (0, 0, *self.screen.get_size()), 1)
