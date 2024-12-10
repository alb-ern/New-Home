import pygame as pg
import numpy as np
from character import Character
from player import Player
Chars = Character.Chars





class INPUT:
    @staticmethod
    def init() -> None:
        for i in Chars:
            if isinstance(i, Player):
                global player
                player = i
    screen_play = False
    screen_ui = True
    is_game_running = True
    _inpc = np.array([0, 0, 0, 0])
    buffer = 6

    def __init__(self) -> None:
        INPUT.click = False
        INPUT.press = pg.key.get_pressed()
      # Main Loop
        self.player_input()
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
                    # game.update(event)#Main update  w single sgtroke
                    pass
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                INPUT.click = True

    def player_input(self) -> None:
        INPUT._inpc = np.maximum(INPUT._inpc-1, 0)
        if INPUT.press[pg.K_w]:
            pass
        if INPUT.press[pg.K_UP] and INPUT._inpc[0] == 0:
            player.loc[1] -= 1 if player.loc[1] > 0 else 0
            INPUT._inpc[0] += INPUT.buffer
        if INPUT.press[pg.K_DOWN] and INPUT._inpc[1] == 0:
            player.loc[1] += 1 if player.loc[1] < 11 else 0
            INPUT._inpc[1] += INPUT.buffer
        if INPUT.press[pg.K_RIGHT] and INPUT._inpc[2] == 0:
            player.loc[0] += 1 if player.loc[0] < 20 else 0
            INPUT._inpc[2] += INPUT.buffer
        if INPUT.press[pg.K_LEFT] and INPUT._inpc[3] == 0:
            player.loc[0] -= 1 if player.loc[0] > 0 else 0
            INPUT._inpc[3] += INPUT.buffer
