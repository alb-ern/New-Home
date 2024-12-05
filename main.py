from loop import LOOP
from gui import GUI
import pygame as pg

gui = GUI()
clock = pg.time.Clock()



class MAIN:
    running = True

    @staticmethod
    def main():
        while LOOP.is_game_running:
            clock.tick(30)
            while LOOP.screen_ui:
                LOOP()
                gui.refresh_ui()
                clock.tick(10)
            while LOOP.screen_play:
                LOOP()
                gui.refresh_game()
                clock.tick(30)
        pg.quit()


if __name__ == "__main__":
    MAIN.main()
