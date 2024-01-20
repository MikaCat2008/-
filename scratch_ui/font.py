from pygame.font import init as init_font, SysFont
from pygame.surface import SurfaceType

init_font()

font = SysFont(None, 32)


def text_render(text: str, color: tuple[int, int, int] = (255, 255, 255)) -> SurfaceType:
    return font.render(text, None, color)
