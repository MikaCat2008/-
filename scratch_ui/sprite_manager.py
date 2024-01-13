from pygame.surface import SurfaceType

from .abstractions import SpriteType
from .sprite import Sprite

from scratch_api.memory import memory
from scratch_api.sprite_manager import SpriteManager as GameSpriteManager

game_sprite_manager = GameSpriteManager()


class SpriteManager:
    sprites: list[SpriteType]
    selected_sprite: SpriteType

    def __init__(self) -> None:
        self.sprites = []
        self.selected_sprite = None

    def create_sprite(
        self, 
        image: SurfaceType
    ) -> SpriteType:
        game_sprite = game_sprite_manager.create_sprite(
            surface = image
        )
        sprite = Sprite(
            game_sprite,
            []
        )

        memory.sprites.append(game_sprite)
        self.sprites.append(sprite)

        return sprite


sprite_manager = SpriteManager()
