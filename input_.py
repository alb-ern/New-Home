import pygame as pg
from character import Character
from player import Player
Chars = Character.Chars


player = Player(hp=30, loc=(1, 1), img="knight")
enemy = Character(img="enemy")


class INPUT:
    screen_play = False
    screen_ui = True
    is_game_running = True

    def __init__(self) -> None:
        INPUT.click = False
      # Main Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                INPUT.screen_play = False
                INPUT.screen_ui = False
                INPUT.is_game_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    INPUT.screen_play = not INPUT.screen_play
                    INPUT.screen_ui = not INPUT.screen_ui
                elif INPUT.screen_play:
                    self.game_action(event)
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                INPUT.click = True

    def game_action(self, event) -> None:
        if event.key == pg.K_RIGHT:
            player.loc[0] += 1 if player.loc[0] < 20 else 0
        elif event.key == pg.K_LEFT:
            player.loc[0] -= 1 if player.loc[0] > 0 else 0
        elif event.key == pg.K_DOWN:
            player.loc[1] += 1 if player.loc[1] < 11 else 0
        elif event.key == pg.K_UP:
            player.loc[1] -= 1 if player.loc[1] > 0 else 0
