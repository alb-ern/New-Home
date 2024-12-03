from loop import LOOP
from gui import GUI
import pygame as pg

gui = GUI()
clock = pg.time.Clock()

class MAIN:
    running=True
    @staticmethod
    def main():
        while LOOP.is_game_running:
            while LOOP.game_active:
                LOOP()
                gui.refresh_game()
                clock.tick(30)
            clock.tick(30)
        pg.quit()


if __name__ == "__main__":
    MAIN.main()
