from ..frame import Frame

from .GameFrame import GameFrame
from .SpritesFrame import SpritesFrame
from .ScriptsFrame import ScriptsFrame

class WindowFrame(Frame):    
    def start(self) -> None:
        self.frames = [
            GameFrame(self.screen, (600, 400), (10, 10)),
            SpritesFrame(self.screen, (600, 320), (10, 420)),
            ScriptsFrame(self.screen, (770, 730), (620, 10))
        ]
