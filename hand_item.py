from item import Item


class _HandItem(Item):
    def __init__(self, damage: float = 2, counter_damage: float = 20) -> None:
        """Item which can be handheld
        damage: pure attack damage
        counter_attack: percentage of damage dealt back
        """
        super().__init__()
        self.damage = damage
        self.counter_damage = damage*counter_damage/100
