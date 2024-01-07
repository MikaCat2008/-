import time

from ..abstractions import Number
from ..motion_block import MotionBlock


class GlideToBlock(MotionBlock):
    seconds: Number
    end_x: Number
    end_y: Number
    original_coords: tuple[float]
    start_time: float

    def __init__(self, seconds: Number, end_x: Number, end_y: Number) -> None:
        super().__init__()

        self.seconds = seconds
        self.end_x = end_x
        self.end_y = end_y
        self.original_coords = None
        self.start_time = time.time()

    def execute(self) -> bool:
        if self.start_time is None:
            self.start_time = time.time()

        if time.time() > self.start_time + float(self.seconds):
            self.start_time = None
            self.original_coords = None

            return True
        
        if self.original_coords is None:
            self.original_coords = self.sprite.coords
        
        k = (time.time() - self.start_time) / float(self.seconds)

        ox, oy = self.original_coords
        ex, ey = self.end_x, self.end_y

        x = ox + (float(ex) - ox) * k
        y = oy + (float(ey) - oy) * k

        self.sprite.coords = x, y

        return False
