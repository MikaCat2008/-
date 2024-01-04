from scratch_api.abstractions import BooleanNodeType
from ..nodes.BooleanNode import BooleanNode


class NotNode(BooleanNode):
    def get_value(self) -> bool:
        return not self.value
