from pygame.surface import Surface, SurfaceType

from .abstractions import Blocks, SpriteType, SpriteManagerType

from .sprite import Sprite
from .memory import memory


class SpriteManager(SpriteManagerType):
    def create_sprite(
        self, 
        blocks: Blocks = None,
        variable_names: list[str] = None,
        name: str = None,
        coords: tuple[float, float] = (0, 0),
        direction: float = 0,
        surface: SurfaceType = None,
        rotation_style: int = 2,
        is_show: bool = True
    ) -> SpriteType:
        return Sprite(
            blocks or [], 
            variable_names or [], 
            name or f"Sprite {len(memory.sprites) + 1}", 
            coords, 
            direction, 
            surface or Surface((32, 32)), 
            rotation_style,
            is_show
        )
