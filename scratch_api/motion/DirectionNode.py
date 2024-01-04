from ..nodes.NumberNode import NumberNode


class DirectionNode(NumberNode):
    def get_value(self) -> float:
        return self.sprite.direction
