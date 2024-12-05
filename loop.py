import pygame as pg
from character import Character
from player import Player
Chars = Character.Chars


player = Player(hp=30, loc=(1, 1), img="knight")
enemy = Character(img="enemy")


class LOOP:
    screen_play = False
    screen_ui = True
    is_game_running = True

    def __init__(self) -> None:
        LOOP.click=False
      # Main Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                LOOP.screen_play = False
                LOOP.screen_ui = False
                LOOP.is_game_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    LOOP.screen_play = not LOOP.screen_play
                    LOOP.screen_ui = not LOOP.screen_ui
                elif LOOP.screen_play:
                    self.game_action(event)
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                LOOP.click=True


    def game_action(self, event) -> None:
        if event.key == pg.K_RIGHT:
            player.loc[0] += 1
        elif event.key == pg.K_LEFT:
            player.loc[0] -= 1
        elif event.key == pg.K_DOWN:
            player.loc[1] += 1
        elif event.key == pg.K_UP:
            player.loc[1] -= 1
