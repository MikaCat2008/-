from pygame.time import Clock
from pygame.event import get as get_events
from pygame.image import load as load_picture
from pygame.display import set_mode, set_caption
from pygame.transform import scale_by

from scratch_api import set_screen, set_sprites, start, update
from scratch_api.block_container import BlockContainer

from scratch_api.nodes import NumberNode
from scratch_api.nodes import StringNode
from scratch_api.nodes import BooleanNode
from scratch_api.nodes import VariableNode

# motion
from scratch_api.motion import MoveBlock
from scratch_api.motion import TurnRightBlock
from scratch_api.motion import TurnLeftBlock

from scratch_api.motion import PointInDirectionBlock
from scratch_api.motion import PointTowardsBlock

from scratch_api.motion import GoToXYBlock
from scratch_api.motion import GoToBlock
from scratch_api.motion import GlideToBlock

from scratch_api.motion import ChangeXByBlock
from scratch_api.motion import SetXToBlock
from scratch_api.motion import ChangeYByBlock
from scratch_api.motion import SetYToBlock

from scratch_api.motion import IfOnEdgeBounceBlock

from scratch_api.motion import SetRotationStyleBlock

from scratch_api.motion import XPositionNode
from scratch_api.motion import YPositionNode
from scratch_api.motion import DirectionNode

# looks
from scratch_api.looks import ShowBlock
from scratch_api.looks import HideBlock

# sound

# pen
from scratch_api.pen import ClearBlock

from scratch_api.pen import StampBlock

from scratch_api.pen import PenDownBlock
from scratch_api.pen import PenUpBlock

# data
from scratch_api.data import SetValueToBlock
from scratch_api.data import ChangeValueByBlock

# events
from scratch_api.events import OnStartBlock
from scratch_api.events import OnKeyPressBlock

# control
from scratch_api.control import WaitBlock

from scratch_api.control import RepeatBlock
from scratch_api.control import ForeverBlock

from scratch_api.control import IfThenBlock
from scratch_api.control import IfThenElseBlock
from scratch_api.control import WaitUntilBlock
from scratch_api.control import RepeatUntilBlock

# sensing

# operators
from scratch_api.operators import AddNode
from scratch_api.operators import SubNode
from scratch_api.operators import MulNode
from scratch_api.operators import DivNode

from scratch_api.operators import RandomNumberNode

from scratch_api.operators import LessThanNode
from scratch_api.operators import EqualsToNode
from scratch_api.operators import BiggerThanNode

from scratch_api.operators import AndNode
from scratch_api.operators import OrNode
from scratch_api.operators import NotNode

from scratch_api.operators import MathFuncOfNode

# more blocks

from scratch_api.sprite_manager import SpriteManager

clock = Clock()
screen = set_mode((800, 600))
sprite_manager = SpriteManager()

set_screen(screen)
set_sprites([
    sprite_manager.create_sprite(
        blocks = [
            OnStartBlock([
                GlideToBlock(1, 200, 200)
                
                # GoToXYBlock(200, 300),
                # PenDownBlock(),
                # HideBlock(),

                # ForeverBlock([
                #     MoveBlock(MulNode(10, MathFuncOfNode("sin", VariableNode("i")))),
                #     TurnLeftBlock(1),
                #     ChangeValueByBlock("i", 0.05)
                # ])
            ])
        ],
        variable_names = ["i"],
        name = "Trah-trah",
        surface = load_picture("trah-trah.jpg").convert_alpha()
    )
])

start()

while 1:
    update(get_events())

    set_caption(f"{clock.get_fps():.1f} fps")
    clock.tick(120)
