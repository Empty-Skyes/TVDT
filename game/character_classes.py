class Names:
    def __init__(self, fullname, nickname=None):
        self.fullname = fullname
        self.nickname = nickname
        self.normal_name = fullname.split()[0]  # Use the first name by default
        self.available_names = [self.fullname, self.normal_name]
        if nickname:
            self.available_names.append(nickname)

    def add_name(self, name):
        self.available_names.append(name)

    def __str__(self):
        display_name = self.nickname or self.normal_name
        return f"Display Name: {display_name}, Available Names: {', '.join(self.available_names)}"

class Stats:
    def __init__(self, lvl=1, hp=100, atk=10, defense=5, intelligence=10, resistance=5):
        self.lvl = lvl
        self.base_hp = hp
        self.base_atk = atk
        self.base_defense = defense
        self.base_intelligence = intelligence
        self.base_resistance = resistance

        # Current stats (used during combat)
        self.current_hp = self.base_hp

        # EXP system
        self.current_exp = 0
        self.exp_to_next_level = 1000

    def level_up(self):
        """Increases stats based on level-up scaling."""
        self.lvl += 1
        self.current_exp = 0
        self.exp_to_next_level = 1000  # Reset EXP to the next level

        # Stat increases
        self.base_hp += int(self.base_hp * 0.1)  # +10% HP
        self.base_atk += 2  # +2 ATK per level
        self.base_defense += 1  # +1 DEF per level
        self.base_intelligence += 1  # +1 INT per level
        self.base_resistance += 1  # +1 RES per level

        # Restore HP to full after leveling up
        self.current_hp = self.base_hp

    def gain_exp(self, amount):
        """Adds EXP and handles leveling up."""
        self.current_exp += amount
        while self.current_exp >= self.exp_to_next_level:  # Check for multiple level-ups
            excess_exp = self.current_exp - self.exp_to_next_level
            self.level_up()
            self.current_exp = excess_exp

    def adjust_stat(self, stat, amount):
        """Dynamically adjust stats during combat (e.g., reduce HP)."""
        if stat == "hp":
            self.current_hp = max(0, min(self.base_hp, self.current_hp + amount))
        elif stat == "atk":
            self.base_atk = max(0, self.base_atk + amount)
        elif stat == "defense":
            self.base_defense = max(0, self.base_defense + amount)
        elif stat == "intelligence":
            self.base_intelligence = max(0, self.base_intelligence + amount)
        elif stat == "resistance":
            self.base_resistance = max(0, self.base_resistance + amount)
        else:
            raise ValueError(f"Invalid stat: {stat}")

    def __str__(self):
        return (f"Level: {self.lvl}, HP: {self.current_hp}/{self.base_hp}, ATK: {self.base_atk}, "
                f"DEF: {self.base_defense}, INT: {self.base_intelligence}, RES: {self.base_resistance}, "
                f"EXP: {self.current_exp}/{self.exp_to_next_level}")

class CombatEquipment:
    def __init__(self, weapon=None, armor=None, accessory=None):
        self.weapon = weapon
        self.armor = armor
        self.accessory = accessory

    def __str__(self):
        return (f"Weapon: {self.weapon or 'None'}, Armor: {self.armor or 'None'}, "
                f"Accessory: {self.accessory or 'None'}")

class RelationshipManager:
    def __init__(self, pc_name):
        self.pc_name = pc_name  # Player Character name for LP tracking
        self.allies = {}
        self.enemies = {}
        self.family = {}
        self.love_points = 50  # Initial LP toward the PC

    def adjust_lp(self, amount):
        self.love_points = max(0, min(100, self.love_points + amount))  # LP is clamped between 0 and 100

    def set_relationship(self, category, character_name):
        if category not in ["allies", "enemies", "family"]:
            raise ValueError("Invalid relationship category.")
        getattr(self, category)[character_name] = True  # Mark as ally, enemy, or family

    def __str__(self):
        def format_relationships(category):
            return ", ".join(category.keys()) or "None"

        return (f"Love Points (toward {self.pc_name}): {self.love_points}\n"
                f"Allies: {format_relationships(self.allies)}\n"
                f"Enemies: {format_relationships(self.enemies)}\n"
                f"Family: {format_relationships(self.family)}")

class Character:
    def __init__(self, fullname, pc_name, nickname=None):
        self.names = Names(fullname, nickname)
        self.stats = Stats()
        self.combat_equipment = CombatEquipment()
        self.relationship_manager = RelationshipManager(pc_name)

    def gain_exp(self, amount):
        """Adds EXP to the character."""
        self.stats.gain_exp(amount)

    def level_up(self):
        """Triggers the level-up process."""
        self.stats.level_up()

    def adjust_stat(self, stat, amount):
        """Adjust stats dynamically during combat."""
        self.stats.adjust_stat(stat, amount)

    def __str__(self):
        return (f"Names:\n{self.names}\n"
                f"Stats:\n{self.stats}\n"
                f"Combat Equipment:\n{self.combat_equipment}\n"
                f"Relationships:\n{self.relationship_manager}")

def calculate_enemy_exp(player_level, enemy_level):
    """
    Dynamically calculate EXP gained based on level difference.
    - Higher-level enemies give more EXP.
    - Lower-level enemies give reduced EXP.
    """
    base_exp = 200  # Base EXP for an enemy of the same level
    level_difference = enemy_level - player_level

    if level_difference > 0:  # Enemy is higher level
        return base_exp + (50 * level_difference)
    elif level_difference < 0:  # Enemy is lower level
        return max(10, base_exp - (30 * abs(level_difference)))
    else:  # Same level
        return base_exp