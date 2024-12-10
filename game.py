import numpy as np
from character import Character




class Game:
    def __init__(self) -> None:
        Chars = Character.Chars
        for i in Chars:
            if i.name == "player":
                self.player = i
                break
        self.arr = np.zeros((100, 100))






if __name__=="__main__":
    Game()