from input_ import INPUT
from gui import GUI
import pygame as pg

gui = GUI()
clock = pg.time.Clock()


class MAIN:
    running = True

    @staticmethod
    def main() -> None:
        while INPUT.is_game_running:
            clock.tick(30)
            while INPUT.screen_ui:
                INPUT()
                gui.refresh_ui()
                clock.tick(30)
            while INPUT.screen_play:
                INPUT()
                gui.refresh_game()
                clock.tick(30)
        pg.quit()


if __name__ == "__main__":
    MAIN.main()
