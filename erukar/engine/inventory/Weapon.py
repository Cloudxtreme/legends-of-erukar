from erukar.engine.inventory.Item import Item

class Weapon(Item):
    def __init__(self, name="Weapon"):
        super().__init__("weapon", name)
        self.damage = '1d6'
        self.damage_modifier = 'str'

    def roll(self):
        return super().roll(self.damage)
