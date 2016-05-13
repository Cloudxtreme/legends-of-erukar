from pynarpg.inventory.inventory import Inventory

class Armor(Inventory):
    def __init__(self):
        self.armor_class = 10
        self.max_dex_mod = 2
