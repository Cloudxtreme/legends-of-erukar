from pynarpg.inventory.Item import Item

class Weapon(Item):
    def __init__(self):
        super().__init__()
        self.damage = '1d6'
        self.damage_modifier = 'str'

    def roll(self):
        return super().roll(self.damage)
