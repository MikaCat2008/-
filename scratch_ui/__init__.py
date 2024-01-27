from pygame import mouse
from pygame.event import EventType
from pygame.image import load as load_image
from pygame.display import set_mode, flip
from pygame.surface import SurfaceType

from .abstractions import FrameType
from .frames import WindowFrame
from .node_manager import node_manager
from .block_manager import block_manager
from .input_manager import input_manager
from .sprite_manager import sprite_manager

from scratch_api.nodes import NumberNode

from scratch_api.motion import MoveBlock

from scratch_api.events import OnStartBlock

from scratch_api.control import RepeatBlock

from scratch_api.operators import AddNode
from scratch_api.operators import SubNode
from scratch_api.operators import MulNode
from scratch_api.operators import DivNode

WINDOW_SIZE = (1400, 750)

__scratch_version__ = 0, 3


class Window:
    screen: SurfaceType
    window_frame: FrameType

    def __init__(self, screen: SurfaceType) -> None:
        self.screen = screen
        self.window_frame = WindowFrame(screen, screen.get_size(), (0, 0))

        sprite_manager.selected_sprite = sprite = sprite_manager.create_sprite(
            load_image("artem.jpg").convert_alpha()
        )

        on_start_block = sprite.add_block(
            (100, 100),
            OnStartBlock([])
        )

        # on_start_block.add_block(
        #     block_manager.create_block(
        #         sprite, None, MoveBlock(AddNode(NumberNode(10), NumberNode(4)))
        #     ), 0
        # )
        # on_start_block.add_block(
        #     block_manager.create_block(
        #         sprite, None, MoveBlock(SubNode(NumberNode(10), NumberNode(4)))
        #     ), 0
        # )
        # on_start_block.add_block(
        #     block_manager.create_block(
        #         sprite, None, MoveBlock(MulNode(NumberNode(10), NumberNode(4)))
        #     ), 0
        # )
        # on_start_block.add_block(
        #     block_manager.create_block(
        #         sprite, None, MoveBlock(DivNode(NumberNode(10), NumberNode(4)))
        #     ), 0
        # )

        repeat_block0 = on_start_block.add_block(
            block_manager.create_block(
                # sprite, None, RepeatBlock(AddNode(NumberNode(20), NumberNode(20)), [])
                sprite, None, RepeatBlock(AddNode(NumberNode(20), AddNode(NumberNode(5), NumberNode(20))), [])
            ), 0
        )
        repeat_block1 = repeat_block0.add_block(
            block_manager.create_block(
                sprite, None, RepeatBlock(NumberNode(400), [])
            ), 1
        )

        repeat_block0.add_block(
            block_manager.create_block(
                sprite, None, MoveBlock(NumberNode(3))
            ), 1
        )
        repeat_block0.add_block(
            block_manager.create_block(
                sprite, None, MoveBlock(NumberNode(4))
            ), 1
        )

        repeat_block1.add_block(
            block_manager.create_block(
                sprite, None, MoveBlock(NumberNode(5))
            ), 1
        )
        repeat_block1.add_block(
            block_manager.create_block(
                sprite, None, MoveBlock(NumberNode(6))
            ), 1
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
