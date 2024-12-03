from loop import LOOP
from gui import GUI
import pygame as pg

gui = GUI()
clock = pg.time.Clock()


def main():
    while LOOP.active:
        LOOP()
        gui.refresh()
        clock.tick(30)
    pg.quit()


if __name__ == "__main__":
    main()
