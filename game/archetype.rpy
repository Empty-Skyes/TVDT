init python:
    class Archetype:
        def __init__(self, name, stat_modifiers):
            self.name = name
            self.stat_modifiers = stat_modifiers

        def __str__(self):
            return f"{self.name}"

    attacker = Archetype(
        "Attacker",
        {
            "hp": 0.3,
            "mp": 0.2,
            "attack": 0.4,
            "defense": 0.2,
            "speed": 0.4,
        }
    )

    berserker = Archetype(
        "Berserker",
        {
            "hp": 0.1,
            "mp": 0.1,
            "attack": 0.8,
            "speed": 0.7,
        }
    )

    knight = Archetype(
        "Knight",
        {
            "hp": 0.2,
            "mp": 0.3,
            "attack": 0.3,
            "defense": 0.2,
            "resistance": 0.4,
        }
    )

    archer = Archetype(
        "Archer",
        {
            "hp": 0.3,
            "mp": 0.2,
            "attack": 0.3,
            "resistance": 0.2,
            "speed": 0.8,
        }
    )

    tank = Archetype(
        "Tank",
        {
            "hp": 0.8,
            "mp": 0.1,
            "attack": 0.1,
            "defense": 0.7,
            "resistance": 0.3,
        }
    )

    mage = Archetype(
        "Mage",
        {
            "hp": 0.1,
            "mp": 0.6,
            "intelligence": 0.7,
            "resistance": 0.2,
            "wisdom": 0.3,
        }
    )

    summoner = Archetype(
        "Summoner",
        {
            "hp": 0.3,
            "mp": 0.6,
            "intelligence": 0.4,
            "wisdom": 0.3,
            "speed": 0.6,
        }
    )

    healer = Archetype(
        "Healer",
        {
            "hp": 0.2,
            "mp": 0.7,
            "intelligence": 0.4,
            "wisdom": 0.7,
            "speed": 0.3,
        }
    )



