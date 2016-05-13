from pynarpg.inventory.weapon import Weapon
import unittest

class WeaponTests(unittest.TestCase):
    def test_regex_no_mod(self):
        w = Weapon()
        num, die = w.regex()
        self.assertEqual(num, 1)
        self.assertEqual(die, 6)

    def test_regex_with_mod(self):
        w = Weapon()
        w.damage = '1d10-2'
        num, die, mod = w.regex()
        self.assertEqual(num, 1)
        self.assertEqual(die, 10)
        self.assertEqual(mod, -2)
