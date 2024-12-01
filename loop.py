import pygame as pg
from character import Character
from player import Player
from gui import GUI
Chars = Character.Chars


player = Player(hp=30, loc=(2, 2), img="knight")
enemy = Character()
gui = GUI()
active = True
clock = pg.time.Clock()
while active:  # Main Loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            active = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                pass

    gui.refresh()

    clock.tick(30)
pg.quit()
