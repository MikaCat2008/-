# nodes
from .nodes import NumberNode

# motion
from .motion import MoveBlock
from .motion import TurnRightBlock
from .motion import TurnLeftBlock

# events
from .events import OnStartBlock

# control
from .control import RepeatBlock

# operators
from .operators import AddNode
from .operators import SubNode
from .operators import MulNode
from .operators import DivNode


from scratch_api.objects import (
    # nodes
    NumberNode as NumberGameNode,

    # motion
    MoveBlock as MoveGameBlock,
    TurnRightBlock as TurnRightGameBlock,
    TurnLeftBlock as TurnLeftGameBlock,

    # events
    OnStartBlock as OnStartGameBlock,

    # control
    RepeatBlock as RepeatGameBlock,

    # operators
    AddNode as AddGameNode,
    SubNode as SubGameNode,
    MulNode as MulGameNode,
    DivNode as DivGameNode
)


objects = {
    # nodes
    NumberGameNode: NumberNode,

    # motion
    MoveGameBlock: MoveBlock,
    TurnRightGameBlock: TurnRightBlock,
    TurnLeftGameBlock: TurnLeftBlock,

    # events
    OnStartGameBlock: OnStartBlock,

    # controls
    RepeatGameBlock: RepeatBlock,

    # operators
    AddGameNode: AddNode,
    SubGameNode: SubNode,
    MulGameNode: MulNode,
    DivGameNode: DivNode
}
