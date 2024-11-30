from character import Character


class Player(Character):
	def __init__(self, hp: float = 20, speed: float = 2, loc: tuple[int, int] = (1,1)) -> None:
		super().__init__(hp, speed, loc)