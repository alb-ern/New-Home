from item import Item



class _Armor(Item):
	def __init__(self,defense:float=10) -> None:
		super().__init__()
		self.defense=defense/100