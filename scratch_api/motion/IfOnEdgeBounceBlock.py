from ..memory import memory
from ..motion_block import MotionBlock


class IfOnEdgeBounceBlock(MotionBlock):
    def execute(self) -> bool:
        screen_w, screen_h = memory.screen.get_size()
        sprite_x, sprite_y = self.sprite.coords
        sprite_w, sprite_h = self.sprite.rendered_surface.get_size()

        direction = self.sprite.direction

        if sprite_x - sprite_w / 2 <= 0 or sprite_x + sprite_w / 2 >= screen_w:
            if 0 <= direction <= 180:
                direction = 180 - direction
            elif 180 <= direction <= 360:
                direction = 540 - direction
        elif sprite_y - sprite_h / 2 <= 0 or sprite_y + sprite_h / 2 >= screen_h:
            direction = 360 - direction

        if direction != self.sprite.direction:
            self.sprite.set_direction(direction)

        return True
