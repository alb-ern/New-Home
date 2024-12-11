from input_ import INPUT
from gui import GUI
from character import Character
from player import Player
from game import Game
import pygame as pg


clock = pg.time.Clock()
###chars init here
player = Player(name="player", hp=30, loc=(10, 5), img="knight")
enemy = Character(name="enemy", img="enemy")
###
game = Game()
gui = GUI(game)
INPUT.init()


class Main:
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
                game.arr_update()
                gui.refresh_game()
                clock.tick(30)


def main():
    Main.main()
    pg.quit


if __name__ == "__main__":
    main()
