from pygame.draw import line

from .block import Block
from .memory import memory


class MotionBlock(Block):
    def execute(self, last_coords: tuple[float, float]) -> bool:
        if self.sprite.pen.is_down:
            line(
                memory.stamp_screen, 
                self.sprite.pen.color, 
                last_coords,
                self.sprite.coords,
                self.sprite.pen.size
            )

        return True