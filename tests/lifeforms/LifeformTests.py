from pynarpg.lifeforms.lifeform import Lifeform
import unittest

class LifeformTests(unittest.TestCase):
    def test_define_stats_no_entry(self):
        # Test Case: -2 -2 -2
        l = Lifeform()

        l.define_stats()
        self.assertEqual(l.attributes['str'], -2)
        self.assertEqual(l.attributes['dex'], -2)
        self.assertEqual(l.attributes['vit'], -2)

    def test_define_stats_stronly(self):
        # Test Case: 2 -2 -2
        l = Lifeform()
        l.define_stats(strength=2)
        self.assertEqual(l.attributes['str'], 2)
        self.assertEqual(l.attributes['dex'], -2)
        self.assertEqual(l.attributes['vit'], -2)

    def test_define_stats_dexonly(self):
        # Test Case: 2 -2 -2
        l = Lifeform()
        l.define_stats(dexterity=2)
        self.assertEqual(l.attributes['str'], -2)
        self.assertEqual(l.attributes['dex'], 2)
        self.assertEqual(l.attributes['vit'], -2)

    def test_define_stats_vitonly(self):
        # Test Case: 2 -2 -2
        l = Lifeform()
        l.define_stats(vitality=2)
        self.assertEqual(l.attributes['str'], -2)
        self.assertEqual(l.attributes['dex'], -2)
        self.assertEqual(l.attributes['vit'], 2)
