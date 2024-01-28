# nodes
from .nodes import NumberNode
from .nodes import StringNode
from .nodes import BooleanNode
from .nodes import VariableNode

# motion
from .motion import MoveBlock
from .motion import TurnRightBlock
from .motion import TurnLeftBlock

from .motion import GoToXYBlock

# pen
from .pen import PenDownBlock

# data
from .data import ChangeValueByBlock

# events
from .events import OnStartBlock

# control
from .control import RepeatBlock

from .control import IfThenBlock

# operators
from .operators import AddNode
from .operators import SubNode
from .operators import MulNode
from .operators import DivNode

from .operators import MathFuncOfNode


from scratch_api.objects import (
    # nodes
    NumberNode as NumberGameNode,
    StringNode as StringGameNode,
    BooleanNode as BooleanGameNode,
    VariableNode as VariableGameNode,

    # motion
    MoveBlock as MoveGameBlock,
    TurnRightBlock as TurnRightGameBlock,
    TurnLeftBlock as TurnLeftGameBlock,

    GoToXYBlock as GoToXYGameBlock,

    # pen
    PenDownBlock as PenDownGameBlock,

    # data
    ChangeValueByBlock as ChangeValueByGameBlock,

    # events
    OnStartBlock as OnStartGameBlock,

    # control
    RepeatBlock as RepeatGameBlock,

    IfThenBlock as IfThenGameBlock,

    # operators
    AddNode as AddGameNode,
    SubNode as SubGameNode,
    MulNode as MulGameNode,
    DivNode as DivGameNode,

    MathFuncOfNode as MathFuncOfGameNode
)

objects = {
    # nodes
    NumberGameNode: NumberNode,
    StringGameNode: StringNode,
    BooleanGameNode: BooleanNode,
    VariableGameNode: VariableNode,

    # motion
    MoveGameBlock: MoveBlock,
    TurnRightGameBlock: TurnRightBlock,
    TurnLeftGameBlock: TurnLeftBlock,

    GoToXYGameBlock: GoToXYBlock,

    # pen
    PenDownGameBlock: PenDownBlock,

    # data
    ChangeValueByGameBlock: ChangeValueByBlock,

    # events
    OnStartGameBlock: OnStartBlock,

    # controls
    RepeatGameBlock: RepeatBlock,

    IfThenGameBlock: IfThenBlock,

    # operators
    AddGameNode: AddNode,
    SubGameNode: SubNode,
    MulGameNode: MulNode,
    DivGameNode: DivNode,

    MathFuncOfGameNode: MathFuncOfNode
}
