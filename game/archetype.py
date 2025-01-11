class Archetype:
    def __init__(self, name, speed_bonus=0, aggression=0, defense=0):
        self.name = name
        self.speed_bonus = speed_bonus  # Speed bonus for determining turn order
        self.aggression = aggression  # How aggressively they attack
        self.defense = defense  # How defensively they act

    def apply_behavior(self, character):
        # Adjust the character's stats based on archetype
        character.stats.adjust_stat("atk", self.aggression)
        character.stats.adjust_stat("defense", self.defense)
        character.stats.adjust_stat("atk", self.speed_bonus)  # Speed bonus affects action order
