# nodes
from .nodes import NumberNode
from .nodes import StringNode
from .nodes import BooleanNode
from .nodes import VariableNode

# motion
from .motion import MoveBlock
from .motion import TurnRightBlock
from .motion import TurnLeftBlock

from .motion import PointInDirectionBlock
from .motion import PointTowardsBlock

from .motion import GoToXYBlock
from .motion import GoToBlock
from .motion import GlideToBlock

from .motion import ChangeXByBlock
from .motion import SetXToBlock
from .motion import ChangeYByBlock
from .motion import SetYToBlock

from .motion import IfOnEdgeBounceBlock

from .motion import SetRotationStyleBlock

from .motion import XPositionNode
from .motion import YPositionNode
from .motion import DirectionNode

# looks
from .looks import ShowBlock
from .looks import HideBlock

# sounds

# pen
from .pen import ClearBlock

from .pen import StampBlock

from .pen import PenDownBlock
from .pen import PenUpBlock

# data
from .data import SetValueToBlock
from .data import ChangeValueByBlock

# events
from .events import OnStartBlock
from .events import OnKeyPressBlock

# control
from .control import WaitBlock

from .control import RepeatBlock
from .control import ForeverBlock

from .control import IfThenBlock
from .control import IfThenElseBlock
from .control import WaitUntilBlock
from .control import RepeatUntilBlock

# operators
from .operators import AddNode
from .operators import SubNode
from .operators import MulNode
from .operators import DivNode

from .operators import RandomNumberNode

from .operators import LessThanNode
from .operators import EqualsToNode
from .operators import BiggerThanNode

from .operators import AndNode
from .operators import OrNode
from .operators import NotNode

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

    PointInDirectionBlock as PointInDirectionGameBlock,
    PointTowardsBlock as PointTowardsGameBlock,
    
    GoToXYBlock as GoToXYGameBlock,
    GoToBlock as GoToGameBlock,
    GlideToBlock as GlideToGameBlock,

    ChangeXByBlock as ChangeXByGameBlock,
    SetXToBlock as SetXToGameBlock,
    ChangeYByBlock as ChangeYByGameBlock,
    SetYToBlock as SetYToGameBlock,

    IfOnEdgeBounceBlock as IfOnEdgeBounceGameBlock,

    SetRotationStyleBlock as SetRotationStyleGameBlock,

    XPositionNode as XPositionGameNode,
    YPositionNode as YPositionGameNode,
    DirectionNode as DirectionGameNode,

    ShowBlock as ShowGameBlock,
    HideBlock as HideGameBlock,

    # sounds

    # pen
    ClearBlock as ClearGameBlock,

    StampBlock as StampGameBlock,

    PenDownBlock as PenDownGameBlock,
    PenUpBlock as PenUpGameBlock,

    # data
    SetValueToBlock as SetValueToGameBlock,
    ChangeValueByBlock as ChangeValueByGameBlock,

    # events
    OnStartBlock as OnStartGameBlock,
    OnKeyPressBlock as OnKeyPressGameBlock,

    # control
    WaitBlock as WaitGameBlock,

    RepeatBlock as RepeatGameBlock,
    ForeverBlock as ForeverGameBlock,

    IfThenBlock as IfThenGameBlock,
    IfThenElseBlock as IfThenElseGameBlock,
    WaitUntilBlock as WaitUntilGameBlock,
    RepeatUntilBlock as RepeatUntilGameBlock,

    # operators
    AddNode as AddGameNode,
    SubNode as SubGameNode,
    MulNode as MulGameNode,
    DivNode as DivGameNode,

    RandomNumberNode as RandomNumberGameNode,

    LessThanNode as LessThanGameNode,
    EqualsToNode as EqualsToGameNode,
    BiggerThanNode as BiggerThanGameNode,

    AndNode as AndGameNode,
    OrNode as OrGameNode,
    NotNode as NotGameNode,

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

    PointInDirectionGameBlock: PointInDirectionBlock,
    PointTowardsGameBlock: PointTowardsBlock,

    GoToXYGameBlock: GoToXYBlock,
    GoToGameBlock: GoToBlock,
    GlideToGameBlock: GlideToBlock,

    ChangeXByGameBlock: ChangeXByBlock,
    SetXToGameBlock: SetXToBlock,
    ChangeYByGameBlock: ChangeYByBlock,
    SetYToGameBlock: SetYToBlock,

    IfOnEdgeBounceGameBlock: IfOnEdgeBounceBlock,

    SetRotationStyleGameBlock: SetRotationStyleBlock,

    XPositionGameNode: XPositionNode,
    YPositionGameNode: YPositionNode,
    DirectionGameNode: DirectionNode,

    # loocks
    ShowGameBlock: ShowBlock,
    HideGameBlock: HideBlock,

    # pen
    ClearGameBlock: ClearBlock,

    StampGameBlock: StampBlock,

    PenDownGameBlock: PenDownBlock,
    PenUpGameBlock: PenUpBlock,

    # data
    SetValueToGameBlock: SetValueToBlock,
    ChangeValueByGameBlock: ChangeValueByBlock,

    # events
    OnStartGameBlock: OnStartBlock,
    OnKeyPressGameBlock: OnKeyPressBlock,

    # controls
    WaitGameBlock: WaitBlock,

    RepeatGameBlock: RepeatBlock,
    ForeverGameBlock: ForeverBlock,

    IfThenGameBlock: IfThenBlock,
    IfThenElseGameBlock: IfThenElseBlock,
    WaitUntilGameBlock: WaitUntilBlock,
    RepeatUntilGameBlock: RepeatUntilBlock,

    # operators
    AddGameNode: AddNode,
    SubGameNode: SubNode,
    MulGameNode: MulNode,
    DivGameNode: DivNode,

    RandomNumberGameNode: RandomNumberNode,

    LessThanGameNode: LessThanNode,
    EqualsToGameNode: EqualsToNode,
    BiggerThanGameNode: BiggerThanNode,

    AndGameNode: AndNode,
    OrGameNode: OrNode,
    NotGameNode: NotNode,

    MathFuncOfGameNode: MathFuncOfNode
}
