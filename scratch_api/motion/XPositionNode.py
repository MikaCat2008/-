from ..nodes.NumberNode import NumberNode


class XPositionNode(NumberNode):
    def get_value(self) -> float:
        return self.sprite.coords[0]
