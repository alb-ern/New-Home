import pygame as pg
from character import Character
from player import Player
Chars = Character.Chars


player = Player(hp=30, loc=(1, 1), img="knight")
enemy = Character(img="enemy")


class LOOP:
    game_active = True
    is_game_running = True

    def __init__(self) -> None:
      # Main Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                LOOP.game_active = False
                LOOP.is_game_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    player.loc[0] += 1
                elif event.key == pg.K_LEFT:
                    player.loc[0] -= 1
                elif event.key == pg.K_DOWN:
                    player.loc[1] += 1
                elif event.key == pg.K_UP:
                    player.loc[1] -= 1
