import math

from ..abstractions import String, Boolean
from ..block import Block

from pygame.mouse import get_pos


def angle(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    x1, y1 = point1
    x2, y2 = point2

    x, y = x2 - x1, y1 - y2
    
    if x == 0:
        if y >= 0:
            return 90
        return -90
    if y == 0:
        if x >= 0:
            return 0
        return 180

    angle = math.atan(y / x) * 180 / math.pi

    if x > 0 and y > 0:
        return angle
    elif x < 0 and y > 0:
        return 180 - abs(angle)
    elif x < 0 and y < 0:
        return 180 + angle
    elif x > 0 and y < 0:
        return 360 - abs(angle)


class PointTowardsBlock(Block):
    sprite_name: String
    mouse_pointer: Boolean

    def __init__(self, sprite_name: String, mouse_pointer: Boolean) -> None:
        super().__init__()

        self.sprite_name = sprite_name
        self.mouse_pointer = mouse_pointer

    def execute(self) -> bool:
        coords1 = self.sprite.coords

        if bool(self.mouse_pointer):
            coords2 = get_pos()
        else:
            coords2 = self.get_sprite_by_name(str(self.sprite_name)).coords

        self.sprite.set_direction(angle(coords1, coords2))

        return True
