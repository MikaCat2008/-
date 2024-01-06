from pygame.mouse import get_pos

from ..abstractions import String, Boolean
from ..block import Block


class GoToBlock(Block):
    sprite_name: String
    mouse_pointer: Boolean

    def __init__(self, *args: tuple[String, Boolean]) -> None:
        super().__init__(args)

        self.sprite_name = args[0]
        self.mouse_pointer = args[1]

    def execute(self) -> bool:
        if bool(self.mouse_pointer):
            self.sprite.coords = get_pos()
        else:
            sprite = self.get_sprite_by_name(str(self.sprite_name))

            self.sprite.coords = sprite.coords

        return True
