import random

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
    def __init__(self, lvl=1, hp=25, atk=10, defense=5, intelligence=10, resistance=5):
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
        self.is_in_combat = False  # Flag to track if the character is in combat

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

    def start_combat(self, enemy):
        """Initiates combat with the specified enemy."""
        combat_manager = CombatManager(self, enemy)
        return combat_manager

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


class CombatManager:
    def __init__(self, party_manager):
        self.party_manager = party_manager
        self.round = 1

    def player_turn(self, action, player_character):
        """Handle player actions during combat (attack, arte, defend)."""
        if action == "attack":
            return self.attack(player_character, self.party_manager.enemy_party)
        elif action == "arte":
            return self.arte(player_character, self.party_manager.enemy_party)
        elif action == "defend":
            return self.defend(player_character)
        else:
            return "Invalid action"

    def enemy_turn(self):
        """Handle enemy actions during combat (randomized action)."""
        results = []
        for enemy_character in self.party_manager.enemy_party:
            action = random.choice(["attack", "defend"])
            if action == "attack":
                results.append(self.attack(enemy_character, self.party_manager.player_party))
            elif action == "defend":
                results.append(self.defend(enemy_character))
        return results

    def attack(self, attacker, defenders):
        """Calculate damage from an attack on a defender."""
        damage_results = []
        for defender in defenders:
            damage = max(0, attacker.stats.base_atk - defender.stats.base_defense)
            defender.stats.adjust_stat("hp", -damage)
            damage_results.append(f"{attacker.names} attacks {defender.names} for {damage} damage!")
        return damage_results

    def arte(self, attacker, defenders):
        """Calculate damage from an arte (special skill) on defenders."""
        damage_results = []
        for defender in defenders:
            damage = max(0, (attacker.stats.base_intelligence * 1.5) - defender.stats.base_resistance)
            defender.stats.adjust_stat("hp", -damage)
            damage_results.append(f"{attacker.names} uses Arte on {defender.names} for {damage} damage!")
        return damage_results

    def defend(self, defender):
        """Increase the defender's defense temporarily."""
        defender.stats.adjust_stat("defense", 2)  # Temporarily boost defense
        return f"{defender.names} defends, increasing defense!"

    def is_combat_over(self):
        """Check if the combat is over (any party's HP reaches 0)."""
        if all(character.stats.current_hp <= 0 for character in self.party_manager.player_party):
            return "The player party has been defeated!"
        elif all(character.stats.current_hp <= 0 for character in self.party_manager.enemy_party):
            return "The enemy party has been defeated!"
        return None

    def start_combat(self):
        """Start a round of combat, alternating turns between the player and enemies."""
        results = []
        while True:
            # Player turn for each character in the player's party
            for character in self.party_manager.player_party:
                action = random.choice(["attack", "arte", "defend"])  # Random action for now
                results.extend(self.player_turn(action, character))

            # Check if combat is over after player's turn
            combat_status = self.is_combat_over()
            if combat_status:
                results.append(combat_status)
                break

            # Enemy turn
            results.extend(self.enemy_turn())

            # Check if combat is over after enemy's turn
            combat_status = self.is_combat_over()
            if combat_status:
                results.append(combat_status)
                break

            # Increment round counter
            self.round += 1

        return results

class PartyManager:
    def __init__(self):
        self.player_party = []  # List to hold the player party (up to 3 characters)
        self.enemy_party = []  # List to hold the enemy party (up to 6 characters or monsters)

    def add_to_player_party(self, character):
        """Add a character to the player's party."""
        if len(self.player_party) < 3:
            self.player_party.append(character)
        else:
            raise ValueError("Player party is full (max 3 characters).")

    def add_to_enemy_party(self, character):
        """Add a character or monster to the enemy's party."""
        if len(self.enemy_party) < 6:
            self.enemy_party.append(character)
        else:
            raise ValueError("Enemy party is full (max 6 characters).")

    def remove_from_player_party(self, character):
        """Remove a character from the player's party."""
        if character in self.player_party:
            self.player_party.remove(character)
        else:
            raise ValueError(f"{character.names} is not in the player's party.")

    def remove_from_enemy_party(self, character):
        """Remove a character from the enemy's party."""
        if character in self.enemy_party:
            self.enemy_party.remove(character)
        else:
            raise ValueError(f"{character.names} is not in the enemy's party.")

    def display_parties(self):
        """Return the current parties as a string."""
        player_party_names = ", ".join([str(member.names) for member in self.player_party]) if self.player_party else "None"
        enemy_party_names = ", ".join([str(member.names) for member in self.enemy_party]) if self.enemy_party else "None"
        return f"Player Party: {player_party_names}\nEnemy Party: {enemy_party_names}"

    def get_combat_parties(self):
        """Return the current parties for combat."""
        return self.player_party, self.enemy_party
