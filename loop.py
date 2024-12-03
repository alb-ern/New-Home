import pygame as pg
from character import Character
from player import Player
Chars = Character.Chars


player = Player(hp=30, loc=(1, 1), img="knight")
enemy = Character(img="enemy")


class LOOP:
	active=True
	def __init__(self) -> None:
	  # Main Loop
		for event in pg.event.get():
			if event.type == pg.QUIT:
				LOOP.active = False
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_RIGHT:
					player.loc[0]+=1
				elif event.key == pg.K_LEFT:
					player.loc[0]-=1
				elif event.key == pg.K_DOWN:
					player.loc[1]+=1
				elif event.key == pg.K_UP:
					player.loc[1]-=1

