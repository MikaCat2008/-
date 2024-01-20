from ..node import Node

from scratch_api.abstractions import BooleanNodeType as BooleanGameNodeType


class BooleanNode(Node):
    game_node: BooleanGameNodeType
