from pygame.event import EventType
from ..frame import Frame

from .GameFrame import GameFrame
from .SpritesFrame import SpritesFrame
from .ScriptsFrame import ScriptsFrame

from ..block_manager import block_manager


class WindowFrame(Frame):    
    def start(self) -> None:
        self.frames = [
            GameFrame(self.screen, (600, 400), (10, 10)),
            SpritesFrame(self.screen, (600, 320), (10, 420)),
            ScriptsFrame(self.screen, (770, 730), (620, 10))
        ]

    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        block = block_manager.selected_block
    
        if block:
            bx, by = block.coords

            self.screen.blit(block.render(), (bx + 820, by + 10))
