import numpy as np
from character import Character


class Game:
    def __init__(self) -> None:
        self.Chars = Character.Chars
        for i in self.Chars:
            if i.name == "player":
                self.player = i
                break
        # str longer than 6 is cut from 6th element
        self.arr = np.zeros(shape=(100, 100), dtype="<U6")
        self.arr_update()

    def arr_update(self) -> None:
        for char in self.Chars:
            self.arr[char.loc[0]][char.loc[1]] = char.name


if __name__ == "__main__":
    self = Game()
    print(self.arr)
    