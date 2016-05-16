from pynarpg.model.RpgEntity import RpgEntity
import unittest

class RpgEntityTests(unittest.TestCase):
    def test_regex_no_mod(self):
        w = RpgEntity()
        num, die, mod = w.regex('1d6')
        self.assertEqual(num, 1)
        self.assertEqual(die, 6)
        self.assertEqual(mod, 0)

    def test_regex_with_mod(self):
        w = RpgEntity()
        num, die, mod = w.regex('1d10-2')
        self.assertEqual(num, 1)
        self.assertEqual(die, 10)
        self.assertEqual(mod, -2)
