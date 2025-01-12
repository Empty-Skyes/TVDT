init python:
    class PartyManager:
        def __init__(self):
            self.player_party = []
            self.enemy_party = []

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
                raise ValueError(f"{character.names.fullname} is not in the player's party.")

        def remove_from_enemy_party(self, character):
            """Remove a character from the enemy's party."""
            if character in self.enemy_party:
                self.enemy_party.remove(character)
            else:
                raise ValueError(f"{character.names.fullname} is not in the enemy's party.")

        def display_player_party(self):
            """Return the current player's party as a string, displaying only full names."""
            return ", ".join([member.names.fullname for member in self.player_party]) if self.player_party else "None"

        def display_parties(self):
            """Return the current parties as a string."""
            player_party_names = self.display_player_party()
            enemy_party_names = ", ".join([member.names.fullname for member in self.enemy_party]) if self.enemy_party else "None"
            return f"Player Party: {player_party_names}\nEnemy Party: {enemy_party_names}"

        def get_combat_parties(self):
            """Return the current parties for combat."""
            return self.player_party, self.enemy_party