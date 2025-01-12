init python:
    import random

    class Stats:
        def __init__(self, lvl=1, hp=25, mp=10, attack=10, defense=5, intelligence=10, resistance=5, wisdom=5, speed=5, aggression=0, archetype=None):
            self.lvl = lvl
            self.base_hp = hp
            self.base_attack = attack
            self.base_defense = defense
            self.base_intelligence = intelligence
            self.base_resistance = resistance
            self.base_wisdom = wisdom
            self.base_speed = speed
            self.aggression = aggression
            self.base_mp = mp
            self.current_hp = self.base_hp
            self.current_mp = self.base_mp
            self.current_exp = 0
            self.exp_to_next_level = 1000
            self.archetype = archetype

            if self.archetype:
                self.apply_archetype_modifiers()

        def apply_archetype_modifiers(self):
            if self.archetype:
                self.base_hp += int(self.base_hp * self.archetype.stat_modifiers.get('hp', 0))
                self.base_attack += int(self.base_attack * self.archetype.stat_modifiers.get('attack', 0))
                self.base_defense += int(self.base_defense * self.archetype.stat_modifiers.get('defense', 0))
                self.base_intelligence += int(self.base_intelligence * self.archetype.stat_modifiers.get('intelligence', 0))
                self.base_resistance += int(self.base_resistance * self.archetype.stat_modifiers.get('resistance', 0))
                self.base_wisdom += int(self.base_wisdom * self.archetype.stat_modifiers.get('wisdom', 0))
                self.base_speed += int(self.base_speed * self.archetype.stat_modifiers.get('speed', 0))
                self.base_mp += int(self.base_mp * self.archetype.stat_modifiers.get('mp', 0))
            self.current_hp = self.base_hp
            self.current_mp = self.base_mp

        def level_up(self):
            self.lvl += 1
            self.current_exp = 0
            self.exp_to_next_level = 1000

            stats_to_increase = {
                'hp': self.base_hp,
                'attack': self.base_attack,
                'defense': self.base_defense,
                'intelligence': self.base_intelligence,
                'resistance': self.base_resistance,
                'wisdom': self.base_wisdom,
                'speed': self.base_speed,
                'mp': self.base_mp
            }

            for stat, base_value in stats_to_increase.items():
                increment = self.random_stat_increment(stat)
                if stat == "hp":
                    self.base_hp += increment
                elif stat == "attack":
                    self.base_attack += increment
                elif stat == "defense":
                    self.base_defense += increment
                elif stat == "intelligence":
                    self.base_intelligence += increment
                elif stat == "resistance":
                    self.base_resistance += increment
                elif stat == "wisdom":
                    self.base_wisdom += increment
                elif stat == "speed":
                    self.base_speed += increment
                elif stat == "mp":
                    self.base_mp += increment

            self.current_hp = self.base_hp
            self.current_mp = self.base_mp

        def random_stat_increment(self, stat):
            base_increment = random.randint(1, 3)

            if self.archetype:
                modifier = self.archetype.stat_modifiers.get(stat, 0)
                if modifier > 0:
                    if random.random() < modifier:
                        return base_increment + random.randint(1, 3)
                    else:
                        return base_increment + 1
                else:
                    return base_increment
            else:
                return base_increment

        def gain_exp(self, amount):
            self.current_exp += amount
            while self.current_exp >= self.exp_to_next_level:
                excess_exp = self.current_exp - self.exp_to_next_level
                self.level_up()
                self.current_exp = excess_exp

        def adjust_stat(self, stat, amount):
            if stat == "hp":
                self.current_hp = max(0, min(self.base_hp, self.current_hp + amount))
            elif stat == "attack":
                self.base_attack = max(0, self.base_attack + amount)
            elif stat == "defense":
                self.base_defense = max(0, self.base_defense + amount)
            elif stat == "intelligence":
                self.base_intelligence = max(0, self.base_intelligence + amount)
            elif stat == "resistance":
                self.base_resistance = max(0, self.base_resistance + amount)
            elif stat == "wisdom":
                self.base_wisdom = max(0, self.base_wisdom + amount)
            elif stat == "speed":
                self.base_speed = max(0, self.base_speed + amount)
            elif stat == "aggression":
                self.aggression = max(0, min(100, self.aggression + amount))
            elif stat == "mp":
                self.current_mp = max(0, min(self.base_mp, self.current_mp + amount))
            else:
                raise ValueError(f"Invalid stat: {stat}")

    class Names:
        def __init__(self, fullname, nickname=None, title=None):
            self.fullname = fullname
            self.nickname = nickname
            self.title = title
            self.name = fullname.split()[0]

        def __str__(self):
            display_name = self.nickname or self.name
            if self.title:
                display_name = f"{self.title} {display_name}"
            return display_name

    class GameCharacter:
        def __init__(self, fullname, nickname=None, title=None, archetype=None):
            self.names = Names(fullname, nickname, title)
            self.stats = Stats(archetype=archetype)
            self.equipment = Equipment()
            self.relationship_manager = RelationshipManager()

            if archetype:
                self.stats.apply_archetype_modifiers()

            self.archetype = archetype

        def gain_exp(self, amount):
            self.stats.gain_exp(amount)

        def level_up(self):
            self.stats.level_up()

        def adjust_stat(self, stat, amount):
            self.stats.adjust_stat(stat, amount)
