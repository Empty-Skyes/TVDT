import random

class CombatManager:
    def __init__(self, party_manager):
        self.party_manager = party_manager
        self.round = 1

    def player_turn(self, action, player_character):
        if action == "attack":
            return self.attack(player_character, self.party_manager.enemy_party)
        elif action == "defend":
            return self.defend(player_character)
        elif action == "use_item":
            if player_character.inventory:
                item = random.choice(player_character.inventory)
                return self.use_item(player_character, item)
            else:
                return f"{player_character.name} has no items to use!"
        else:
            return "Invalid action"

    def enemy_turn(self):
        results = []
        for enemy_character in self.party_manager.enemy_party:
            action = random.choice(["attack", "defend", "use_item"])
            if action == "attack":
                results.append(self.attack(enemy_character, self.party_manager.player_party))
            elif action == "defend":
                results.append(self.defend(enemy_character))
            elif action == "use_item":
                if enemy_character.inventory:
                    item = random.choice(enemy_character.inventory)
                    results.append(self.use_item(enemy_character, item))
                else:
                    results.append(f"{enemy_character.name} has no items to use!")
        return results

    def attack(self, attacker, target_party):
        target = random.choice(target_party)
        damage = max(attacker.stats.attack - target.stats.defense, 0)  # Simplified damage calculation
        target.stats.hp -= damage
        target.stats.hp = max(target.stats.hp, 0)
        return f"{attacker.name} attacks {target.name} for {damage} damage!"

    def defend(self, character):
        return f"{character.name} defends!"

    def use_item(self, character, item):
        return f"{character.name} uses {item}!"

    def is_combat_over(self):
        if not self.party_manager.player_party:
            return "The player party has been defeated!"
        elif not self.party_manager.enemy_party:
            return "The enemy party has been defeated!"
        return None

    def start_combat(self):
        results = []
        while True:
            # Player's turn
            for character in self.party_manager.player_party:
                action = random.choice(["attack", "defend", "use_item"])
                results.append(self.player_turn(action, character))

            # Check if combat is over
            combat_status = self.is_combat_over()
            if combat_status:
                results.append(combat_status)
                break

            # Enemy's turn
            for character in self.party_manager.enemy_party:
                action = random.choice(["attack", "defend", "use_item"])
                results.extend(self.enemy_turn())

            # Check if combat is over after enemies' actions
            combat_status = self.is_combat_over()
            if combat_status:
                results.append(combat_status)
                break

            self.round += 1

        return results
