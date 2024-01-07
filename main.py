from pygame.time import Clock
from pygame.event import get as get_events
from pygame.image import load as load_picture
from pygame.display import set_mode, set_caption
from pygame.transform import scale_by

from scratch_api import set_screen, set_sprites, start, update
from scratch_api.block_container import BlockContainer

from scratch_api.nodes.NumberNode import NumberNode
from scratch_api.nodes.StringNode import StringNode
from scratch_api.nodes.BooleanNode import BooleanNode
from scratch_api.nodes.VariableNode import VariableNode

# motion
from scratch_api.motion.MoveBlock import MoveBlock
from scratch_api.motion.TurnRightBlock import TurnRightBlock
from scratch_api.motion.TurnLeftBlock import TurnLeftBlock

from scratch_api.motion.PointInDirectionBlock import PointInDirectionBlock
from scratch_api.motion.PointTowardsBlock import PointTowardsBlock

from scratch_api.motion.GoToXYBlock import GoToXYBlock
from scratch_api.motion.GoToBlock import GoToBlock
from scratch_api.motion.GlideToBlock import GlideToBlock

from scratch_api.motion.ChangeXByBlock import ChangeXByBlock
from scratch_api.motion.SetXToBlock import SetXToBlock
from scratch_api.motion.ChangeYByBlock import ChangeYByBlock
from scratch_api.motion.SetYToBlock import SetYToBlock

from scratch_api.motion.IfOnEdgeBounceBlock import IfOnEdgeBounceBlock

from scratch_api.motion.SetRotationStyleBlock import SetRotationStyleBlock

from scratch_api.motion.XPositionNode import XPositionNode
from scratch_api.motion.YPositionNode import YPositionNode
from scratch_api.motion.DirectionNode import DirectionNode

# looks

# sound

# pen
from scratch_api.pen.ClearBlock import ClearBlock

from scratch_api.pen.StampBlock import StampBlock

# data
from scratch_api.data.SetValueToBlock import SetValueToBlock
from scratch_api.data.ChangeValueByBlock import ChangeValueByBlock

# events
from scratch_api.events.OnStartBlock import OnStartBlock
from scratch_api.events.OnKeyPressBlock import OnKeyPressBlock

# control
from scratch_api.control.WaitBlock import WaitBlock

from scratch_api.control.RepeatBlock import RepeatBlock
from scratch_api.control.ForeverBlock import ForeverBlock

from scratch_api.control.IfThenBlock import IfThenBlock
from scratch_api.control.IfThenElseBlock import IfThenElseBlock
from scratch_api.control.WaitUntilBlock import WaitUntilBlock
from scratch_api.control.RepeatUntilBlock import RepeatUntilBlock

# sensing

# operators
from scratch_api.operators.AddNode import AddNode
from scratch_api.operators.SubNode import SubNode
from scratch_api.operators.MulNode import MulNode
from scratch_api.operators.DivNode import DivNode

from scratch_api.operators.RandomNumberNode import RandomNumberNode

from scratch_api.operators.LessThanNode import LessThanNode
from scratch_api.operators.EqualsToNode import EqualsToNode
from scratch_api.operators.BiggerThanNode import BiggerThanNode

from scratch_api.operators.AndNode import AndNode
from scratch_api.operators.OrNode import OrNode
from scratch_api.operators.NotNode import NotNode

from scratch_api.operators.MathFuncOfNode import MathFuncOfNode

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
                GoToXYBlock(400, 200),

                ForeverBlock([
                    PointTowardsBlock("Trah-trah")
                ])
            ]),

            OnKeyPressBlock("a", [ChangeXByBlock(-5)]),
            OnKeyPressBlock("d", [ChangeXByBlock(5)]),
            OnKeyPressBlock("w", [ChangeYByBlock(5)]),
            OnKeyPressBlock("s", [ChangeYByBlock(-5)])
        ],
        name = "Artem",
        surface = scale_by(load_picture("artem.jpg").convert_alpha(), 0.5)
    ),
    sprite_manager.create_sprite(
        blocks = [
            OnStartBlock([
                ForeverBlock([
                    PointTowardsBlock("Artem"),
                    MoveBlock(5)
                ])
            ])
        ],
        name = "Trah-trah",
        surface = load_picture("trah-trah.jpg").convert_alpha()
    )
])

start()

while 1:
    update(get_events())

    set_caption(f"{clock.get_fps():.1f} fps")
    clock.tick(120)
