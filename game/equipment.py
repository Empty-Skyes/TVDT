class Equipment:
    def __init__(self, weapon=None, armor=None, accessory=None):
        self.weapon = weapon
        self.armor = armor
        self.accessory = accessory

    def __str__(self):
        return (f"Weapon: {self.weapon or 'None'}, Armor: {self.armor or 'None'}, "
                f"Accessory: {self.accessory or 'None'}")
