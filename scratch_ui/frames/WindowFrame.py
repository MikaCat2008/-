from pygame.event import EventType
from ..frame import Frame

from .GameFrame import GameFrame
from .SpritesFrame import SpritesFrame
from .ScriptsFrame import ScriptsFrame

from ..select_manager import select_manager


class WindowFrame(Frame):    
    def start(self) -> None:
        self.frames = [
            GameFrame(self.screen, (600, 400), (10, 10)),
            SpritesFrame(self.screen, (600, 320), (10, 420)),
            ScriptsFrame(self.screen, (770, 730), (620, 10))
        ]

    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        selected_object = select_manager.selected_object
    
        if selected_object:
            bx, by = mouse_coords

            rendered = selected_object.render()

            self.screen.blit(rendered, (bx - rendered.get_width() / 2, by - 10))
