from hand_item import _HandItem
from armor import _Armor


class EQ:

    hand = _HandItem(damage=1)
    sword = _HandItem(damage=4, counter_damage=30)

    cape = _Armor(defense=5)
    helmet = _Armor(defense=10)

