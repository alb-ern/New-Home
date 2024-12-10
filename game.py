import numpy as np
from character import Character




class Game:
    def __init__(self) -> None:
        Chars = Character.Chars
        for i in Chars:
            if i.name == "player":
                self.player = i
                break
        self.arr = np.zeros(shape=(100, 100),dtype="<U6")#str longer than 6 is cut from 6th element
        







if __name__=="__main__":
    Game()