class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, character):
        return f"{character.names} uses {self.name} and {self.effect}!"