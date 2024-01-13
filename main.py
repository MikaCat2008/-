from pygame.time import Clock
from pygame.event import get as get_events
from pygame.display import set_caption

from scratch_ui import window

clock = Clock()

window.start()

while 1:
    window.update(get_events())

    set_caption(f"{clock.get_fps():.1f} fps")
    clock.tick(120)
