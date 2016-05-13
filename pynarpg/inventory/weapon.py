from pynarpg.inventory.inventory import Inventory

class Weapon(Inventory):
    def __init__(self):
        self.damage = '1d6'
        self.damage_modifier = 'str'

    def regex(self):
        return super().regex(self.damage)
