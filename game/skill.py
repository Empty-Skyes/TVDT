class Skill:
    def __init__(self, name, effect, cost=0):
        self.name = name
        self.effect = effect  # This could be a function that applies the skill effect
        self.cost = cost  # The cost of using the skill, e.g., mana points, cooldown

    def use(self, user, target):
        if user.stats.hp >= self.cost:
            self.effect(user, target)
            user.stats.adjust_stat("hp", -self.cost)  # Deduct the cost (e.g., HP or mana)
            return f"{user.names} uses {self.name} on {target.names}"
        else:
            return f"{user.names} doesn't have enough resources to use {self.name}."

def fireball(user, target):
    damage = max(0, (user.stats.intelligence * 2) - target.stats.resistance)
    target.stats.adjust_stat("hp", -damage)
    return f"Fireball hits {target.names} for {damage} damage!"

def heal_skill(user, target):
    healing = 30
    target.stats.adjust_stat("hp", healing)
    return f"{target.names} is healed for {healing} HP."
