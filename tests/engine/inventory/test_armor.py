from pynarpg import *
import unittest

class ArmorTests(unittest.TestCase):
    def test_calculate_armor_class(self):
        armor = Armor()
        armor.max_dex_mod = 2
        dex = 3
        ac = armor.calculate_armor_class(dex)

        self.assertEqual(ac, 14)
