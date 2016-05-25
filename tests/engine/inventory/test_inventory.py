from pynarpg import *
import unittest

class InventoryTests(unittest.TestCase):
    def test_describe_with_suffix(self):
        i = Item()
        i.item_type = 'Bastard Sword'
        i.rarity = 'Uncommon'
        i.suffix = 'of Fire'

        result = i.describe()

        self.assertEqual(result, "Uncommon Bastard Sword of Fire")

    def test_describe_without_suffix(self):
        i = Item()
        i.item_type = 'Bastard Sword'
        i.rarity = 'Uncommon'

        result = i.describe()

        self.assertEqual(result, "Uncommon Bastard Sword")
