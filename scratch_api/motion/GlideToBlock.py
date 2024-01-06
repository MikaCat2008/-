import time

from ..abstractions import Number
from ..block import Block


class GlideToBlock(Block):
    seconds: Number
    end_coords: tuple[Number, Number]
    original_coords: tuple[float]
    start_time: float

    def __init__(self, seconds: Number, end_x: Number, end_y: Number) -> None:
        super().__init__()

        self.seconds = seconds
        self.end_coords = end_x, end_y
        self.original_coords = None
        self.start_time = time.time()

    def execute(self) -> bool:
        if time.time() > self.start_time + float(self.seconds):
            return True
        
        if self.original_coords is None:
            self.original_coords = self.sprite.coords
        
        k = (time.time() - self.start_time) / self.seconds

        ox, oy = self.original_coords
        ex, ey = self.end_coords

        x = ox + (ex - ox) * k
        y = oy + (ey - oy) * k

        self.sprite.coords = x, y

        return False
