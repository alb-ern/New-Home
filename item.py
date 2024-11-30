class Item():
    EQ_props = ("fire", "poison", "heavy", "ranged")

    def __init__(self) -> None:
        self.props = []
        self.importance = 0

    def set_property(self, property: str) -> None:
        if property in self.EQ_props:
            self.props.append(property)

    def set_importance(self, importance: int) -> None:
        self.importance = importance
