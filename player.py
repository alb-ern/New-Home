import pygame as pg
from character import Character



class Player(Character):
    def __init__(self, name: str, hp: float = 20, speed: float = 2, loc: tuple[int, int] = (2,2), img: str = "error") -> None:
        super().__init__(name, hp, speed, loc, img)

    def input(self):
        pass
