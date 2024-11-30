from character import Character
from player import Player
import os


def char_init():
    player = Player(hp=30, loc=(2, 2), img="knight")
    enemy = Character()
    enemy2 = Character()


def clear_terminal() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def Update() -> None:
    clear_terminal()
    for char in Character.Chars:
        char.update()


def main() -> None:

    input()
    Update()
    player.attack(enemy)
    print(f"{player.hp=}\n{enemy.hp=}\n{enemy2.hp=}")
    if not enemy.hp:
        player.attack(enemy2)


if __name__ == "__main__":
    while True:
        main()
