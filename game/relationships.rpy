init python:
    class RelationshipManager:
        def __init__(self):
            self.relationships = {}
            self.love_points = {}

        def adjust_lp(self, character, amount):
            """Adjust love points (LP) between the player and a character."""
            if character not in self.love_points:
                self.love_points[character] = 50

            self.love_points[character] = max(0, min(100, self.love_points[character] + amount))

        def get_lp(self, character):
            """Retrieve love points for the player and another character."""
            return self.love_points.get(character, 50)

        def set_relationship(self, character_1, character_2, category):
            """Set a relationship status between two characters."""
            if category not in ["allies", "enemies", "family"]:
                raise ValueError("Invalid relationship category. Use 'allies', 'enemies', or 'family'.")

            if character_1 not in self.relationships:
                self.relationships[character_1] = {}

            self.relationships[character_1][character_2] = category

        def get_relationship_status(self, character_1, character_2):
            """Get the relationship status between two characters."""
            return self.relationships.get(character_1, {}).get(character_2, "None")