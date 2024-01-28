from pygame import mouse
from pygame.draw import rect
from pygame.event import EventType
from pygame.surface import Surface
from pygame.transform import scale

from ..frame import Frame
from ..input_manager import input_manager

from scratch_api import set_screen, start as start_game, stop as stop_game, update as update_game


class GameFrame(Frame):    
    def start(self) -> None:
        self.m0 = False
        self.game_screen = Surface((1200, 700))
        
        set_screen(self.game_screen)
    
    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        mx, my = mouse_coords

        changes = update_game(events, (mx, my - 40), input_manager.selected_field is None)

        self.screen.blit(scale(self.game_screen, (600, 350)), (0, 40))

        gsw, gsh = self.game_screen.get_size()
        rect(self.screen, (180, 180, 180), (0, 40, gsw / 2, gsh / 2), 1)

        start, stop = False, False

        if mouse.get_pressed()[0]:
            if 2 <= mx <= 38 and 2 <= my <= 38:
                if not self.m0:
                    start_game()

                    self.m0 = True

                start = True
            if 44 <= mx <= 82 and 2 <= my <= 38:
                if not self.m0:
                    stop_game()

                    self.m0 = True

                stop = True

        elif self.m0:
            self.m0 = False

        if start or changes:
            rect(self.screen, (0, 155, 0), (2, 2, 36, 36))
        else:
            rect(self.screen, (0, 185, 0), (2, 2, 36, 36))
        if stop:
            rect(self.screen, (155, 0, 0), (44, 2, 36, 36))
        else:
            rect(self.screen, (185, 0, 0), (44, 2, 36, 36))


        rect(self.screen, (0, 105, 0), (2, 2, 36, 36), 1)
        rect(self.screen, (105, 0, 0), (44, 2, 36, 36), 1)
