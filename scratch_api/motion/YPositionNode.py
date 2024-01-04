from ..nodes.NumberNode import NumberNode


class YPositionNode(NumberNode):
    def get_value(self) -> float:
        return self.sprite.coords[1]
