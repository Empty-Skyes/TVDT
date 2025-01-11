class RelationshipManager:
    def __init__(self, initial_lp):
        self.allies = {}
        self.enemies = {}
        self.family = {}
        self.love_points = max(0, min(250, initial_lp))

    def adjust_lp(self, amount):
        self.love_points = max(0, min(250, self.love_points + amount))

    def set_relationship(self, category, character_name):
        if category not in ["allies", "enemies", "family"]:
            raise ValueError("Invalid relationship category.")
        getattr(self, category)[character_name] = True

    def __str__(self):
        return f"Love Points: {self.love_points}, Allies: {', '.join(self.allies)}, Enemies: {', '.join(self.enemies)}, Family: {', '.join(self.family)}"