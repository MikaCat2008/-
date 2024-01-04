from pygame.time import Clock
from pygame.event import get as get_events
from pygame.image import load as load_picture
from pygame.display import set_mode, set_caption

from scratch_api import set_screen, set_sprites, start, update

from scratch_api.nodes.NumberNode import NumberNode
from scratch_api.nodes.StringNode import StringNode
from scratch_api.nodes.BooleanNode import BooleanNode
from scratch_api.nodes.VariableNode import VariableNode

# motion
from scratch_api.motion.MoveBlock import MoveBlock
from scratch_api.motion.TurnRightBlock import TurnRightBlock
from scratch_api.motion.TurnLeftBlock import TurnLeftBlock

from scratch_api.motion.PointTowardsBlock import PointTowardsBlock

from scratch_api.motion.ChangeXByBlock import ChangeXByBlock
from scratch_api.motion.SetXToBlock import SetXToBlock
from scratch_api.motion.ChangeYByBlock import ChangeYByBlock
from scratch_api.motion.SetYToBlock import SetYToBlock

from scratch_api.motion.XPositionNode import XPositionNode
from scratch_api.motion.YPositionNode import YPositionNode
from scratch_api.motion.DirectionNode import DirectionNode

# looks
from scratch_api.looks.PrintBlock import PrintBlock

# sound

# pen

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
        [
            OnStartBlock([
                ForeverBlock([
                    SetXToBlock(AddNode(
                        NumberNode(200),
                        MulNode(MathFuncOfNode(StringNode("sin"), VariableNode("i")), NumberNode(100))
                    )),
                    SetYToBlock(AddNode(
                        NumberNode(200),
                        MulNode(MathFuncOfNode(StringNode("cos"), VariableNode("i")), NumberNode(100))
                    )),
                    ChangeValueByBlock(StringNode("i"), NumberNode(0.1))
                ])
            ])
        ],
        ["i"],
        "Sprite1",
        (0, 0),
        0,
        load_picture("skittle.jpg").convert_alpha(),
        2
    )
])

start()

while 1:
    update(get_events())

    set_caption(str(clock.get_fps()))
    clock.tick(120)
