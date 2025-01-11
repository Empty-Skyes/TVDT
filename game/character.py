from relation import RelationshipManager
from equipment import Equipment

class Names:
    def __init__(self, fullname, nickname=None):
        self.fullname = fullname
        self.nickname = nickname
        self.normal_name = fullname.split()[0]

    def __str__(self):
        return self.nickname or self.normal_name


class Stats:
    def __init__(self, level=1, hp=25, attack=10, defense=5, intelligence=10, resistance=5, speed=10):
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.intelligence = intelligence
        self.resistance = resistance
        self.speed = speed
        self.current_hp = hp

    def adjust_stat(self, stat, value):
        if stat == "hp":
            self.current_hp = max(0, self.current_hp + value)
        elif stat == "atk":
            self.attack += value
        elif stat == "defense":
            self.defense += value
        elif stat == "intelligence":
            self.intelligence += value
        elif stat == "resistance":
            self.resistance += value
        elif stat == "speed":
            self.speed += value

    def level_up(self):
        self.level += 1
        self.hp += int(self.hp * 0.1)
        self.attack += 2
        self.defense += 1
        self.intelligence += 1
        self.resistance += 1
        self.speed += 1
        self.current_hp = self.hp

    def __str__(self):
        return f"Level: {self.level}, HP: {self.current_hp}/{self.hp}, ATK: {self.attack}, DEF: {self.defense}, INT: {self.intelligence}, RES: {self.resistance}, SPD: {self.speed}"


class Character:
    def __init__(self, fullname, nickname=None, initial_lp=20, archetype=None, equipment=None):
        self.names = Names(fullname, nickname)
        self.relationship_manager = RelationshipManager(initial_lp)
        self.stats = Stats()
        self.inventory = []
        self.archetype = archetype

        # Use Equipment() if no equipment is provided
        self.equipment = equipment if equipment else Equipment()

    def __str__(self):
        return f"Character: {self.names}, Stats: {self.stats}"


class Enemy:
    def __init__(self, fullname, nickname=None):
        self.names = Names(fullname, nickname)
        self.stats = Stats()

    def __str__(self):
        return f"Enemy: {self.names}, Stats: {self.stats}"