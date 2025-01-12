init python:

    import random

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
            defender.stats.adjust_stat("defense", 2)
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
                for character in self.party_manager.player_party:
                    action = random.choice(["attack", "arte", "defend"])
                    results.extend(self.player_turn(action, character))

                combat_status = self.is_combat_over()
                if combat_status:
                    results.append(combat_status)
                    break

                results.extend(self.enemy_turn())

                combat_status = self.is_combat_over()
                if combat_status:
                    results.append(combat_status)
                    break

                self.round += 1

            return results
