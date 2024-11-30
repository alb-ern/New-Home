from character import Character


class Player(Character):
	def __init__(self, hp: float = 20, speed: float = 2, loc: tuple[int, int] = (0,0), img: str = "error") -> None:
		super().__init__(hp, speed, loc, img)