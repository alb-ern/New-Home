from codex import EQ
from hand_item import _HandItem
from armor import _Armor
from item import Item


class Character():
    Chars = set()

    def __init__(self, hp: float = 20, speed: float = 2, loc: tuple[int, int] = (0, 0), img: str = "error") -> None:
        self.img_name = img
        self.max_hp = round(hp, 2)
        self.hp = self.max_hp
        self.alive = True
        self.default_speed = round(speed, 2)
        self.speed = self.default_speed
        self.bag = set()
        self.hand_item = EQ.hand
        self.armor = EQ.cape
        self.loc = [loc[0], loc[1]]
        Character.Chars.add(self)
        self.update()

    @property
    def img_loc(self) -> list[int]:
        img_loc = [self.loc[0]*64, self.loc[1]*64]
        return img_loc

    def take(self, item: "Item") -> None:
        self.bag.add(item)

    def wear(self, item: "Item") -> None:
        if item in self.bag:
            if isinstance(item, _HandItem):
                self.hand_item = item
            elif isinstance(item, _Armor):
                self.armor = item

    def attack(self, target: "Character") -> None:
        if target.alive:
            target.hp = round(target.hp-self.hand_item.damage *
                              (1-target.armor.defense), 2)
            self.hp = round(self.hp-target.hand_item.counter_damage, 2)
            if target.hp <= 0:
                target.alive = False
            self.update()
            target.update()

    def update(self) -> None:
        self.hp = round(self.hp, 2)
        if not self.alive:
            self.attack = None  # type: ignore
            self.wear = None  # type: ignore
            self.take = None  # type: ignore
            self.hp = 0


if __name__ == "__main__":
    test = Character()
    test2 = Character()
    print(test2.hp, test.hp)
    test.attack(test2)
    print(test2.hp, test.hp)
    test.take(EQ.helmet)
    test.wear(EQ.helmet)
    test2.attack(test)
    print(test2.hp, test.hp)
