from pynarpg.lifeforms.Lifeform import Lifeform
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
        # Test Case: -2 2 -2
        l = Lifeform()
        l.define_stats(dexterity=2)
        self.assertEqual(l.attributes['str'], -2)
        self.assertEqual(l.attributes['dex'], 2)
        self.assertEqual(l.attributes['vit'], -2)

    def test_define_stats_vitonly(self):
        # Test Case: -2 -2 2
        l = Lifeform()
        l.define_stats(vitality=2)
        self.assertEqual(l.attributes['str'], -2)
        self.assertEqual(l.attributes['dex'], -2)
        self.assertEqual(l.attributes['vit'], 2)

    def test_define_level_creates_appropriate_health(self):
        l = Lifeform()
        l.define_stats(vitality=0)
        l.define_level(3)
        self.assertEqual(4*3, l.health)
