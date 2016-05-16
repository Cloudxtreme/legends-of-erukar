from pynarpg.inventory.Inventory import Inventory
import unittest

class InventoryTests(unittest.TestCase):
    def test_describe(self):
        i = Inventory()
        i.item_type = 'Bastard Sword'
        i.rarity = 'Uncommon'
        i.suffix = ' of Fire'

        result = i.describe()

        self.assertEqual(result, "Uncommon Bastard Sword of Fire")
