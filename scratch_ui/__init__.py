from pygame import mouse
from pygame.event import EventType
from pygame.image import load as load_image
from pygame.display import set_mode, flip
from pygame.surface import SurfaceType

from .abstractions import FrameType
from .frames import WindowFrame
from .block_manager import block_manager
from .input_manager import input_manager
from .sprite_manager import sprite_manager

WINDOW_SIZE = (1400, 750)

__scratch_version__ = 0, 7


class Window:
    screen: SurfaceType
    window_frame: FrameType

    def __init__(self, screen: SurfaceType) -> None:
        self.screen = screen
        self.window_frame = WindowFrame(screen, screen.get_size(), (0, 0))

        sprite_manager.selected_sprite = sprite_manager.create_sprite(
            load_image("artem.jpg").convert_alpha(), ["i"]
        )

    def start(self) -> None:
        self.window_frame.start()
        self.window_frame.start_frames()

    def update(self, events: list[EventType]) -> None:
        self.screen.fill((245, 245, 245))

        self.window_frame.update_frames(events, mouse.get_pos())
        self.window_frame.update(events, mouse.get_pos())

        input_manager.update()

        flip()


window = Window(set_mode(WINDOW_SIZE))
