from pynarpg.inventory.Item import Item

class Armor(Item):
    def __init__(self):
        super().__init__()
        self.armor_class_modifier = 2
        self.max_dex_mod = 2

    def calculate_armor_class(self, dexterity=0):
        return 10 + self.armor_class_modifier + min(dexterity, self.max_dex_mod)
