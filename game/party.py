class PartyManager:
    def __init__(self):
        self.player_party = []
        self.enemy_party = []

    def add_to_player_party(self, character):
        if len(self.player_party) < 3:
            self.player_party.append(character)
        else:
            raise ValueError("Player party is full (max 3 characters).")

    def add_to_enemy_party(self, enemy):
        if len(self.enemy_party) < 6:
            self.enemy_party.append(enemy)
        else:
            raise ValueError("Enemy party is full (max 6 enemies).")

    def remove_from_player_party(self, character):
        if character in self.player_party:
            self.player_party.remove(character)
        else:
            raise ValueError(f"{character.names} is not in the player's party.")

    def remove_from_enemy_party(self, enemy):
        if enemy in self.enemy_party:
            self.enemy_party.remove(enemy)
        else:
            raise ValueError(f"{enemy.names} is not in the enemy's party.")

    def display_parties(self):
        player_party_names = ", ".join([str(member.names) for member in self.player_party]) if self.player_party else "None"
        enemy_party_names = ", ".join([str(member.names) for member in self.enemy_party]) if self.enemy_party else "None"
        return f"Player Party: {player_party_names}\nEnemy Party: {enemy_party_names}"

    def get_combat_parties(self):
        return self.player_party, self.enemy_party