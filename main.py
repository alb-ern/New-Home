from input_ import INPUT
from gui import GUI
from player import Player
import pygame as pg


clock = pg.time.Clock()
###chars init here
player = Player(name="",hp=30, loc=(1, 1), img="knight")
###
gui = GUI()
class MAIN:
    @staticmethod
    def main() -> None:
        while INPUT.is_game_running:
            clock.tick(30)
            while INPUT.screen_ui:
                INPUT(player)
                gui.refresh_ui()
                clock.tick(30)
            while INPUT.screen_play:
                INPUT(player)
                gui.refresh_game()
                clock.tick(30)
        pg.quit()



def main():
    MAIN.main()



if __name__ == "__main__":
    main()
