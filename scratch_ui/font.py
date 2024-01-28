from pygame import SRCALPHA
from pygame.font import init as init_font, SysFont
from pygame.surface import Surface, SurfaceType

init_font()

font = SysFont(None, 32)


def text_render(
    text: str, 
    color: tuple[int, int, int] = (255, 255, 255),
    background_color: tuple[int, int, int, int] = (0, 0, 0, 0),
    indent: int = 0
) -> SurfaceType:
    text = font.render(str(text), None, color)

    w = text.get_width()
    surface = Surface((w + indent * 2, 23), SRCALPHA, 32)
    surface.fill(background_color)
    surface.blit(text, (indent, 0))

    return surface
