from pynarpg import *
import unittest

class LifeformTests(unittest.TestCase):
    def test_define_stats_no_entry(self):
        # Test Case: -2 -2 -2
        l = Lifeform()

        self.assertEqual(l.strength, -2)
        self.assertEqual(l.dexterity, -2)
        self.assertEqual(l.vitality, -2)

    def test_define_stats_stronly(self):
        # Test Case: 2 -2 -2
        l = Lifeform()
        l.define_stats({ "strength": 2 })
        self.assertEqual(l.strength, 2)
        self.assertEqual(l.dexterity, -2)
        self.assertEqual(l.vitality, -2)

    def test_define_stats_dexonly(self):
        # Test Case: -2 2 -2
        l = Lifeform()
        l.define_stats({ "dexterity": 2 })
        self.assertEqual(l.strength, -2)
        self.assertEqual(l.dexterity, 2)
        self.assertEqual(l.vitality, -2)

    def test_define_stats_vitonly(self):
        # Test Case: -2 -2 2
        l = Lifeform()
        l.define_stats({ "vitality": 2 })
        self.assertEqual(l.strength, -2)
        self.assertEqual(l.dexterity, -2)
        self.assertEqual(l.vitality, 2)

    def test_define_level_creates_appropriate_health(self):
        l = Lifeform()
        l.define_stats({ "vitality": 0 })
        l.define_level(3)
        self.assertEqual(4*3, l.health)

    def test_take_damage_not_fatal(self):
        l = Lifeform()
        l.define_stats({ "vitality": 2 })
        l.define_level(3)

        l.take_damage(4)
        self.assertTrue('dying' not in l.afflictions)

    def test_take_damage_fatal(self):
        l = Lifeform()
        l.define_stats({ "vitality": 0 })
        l.define_level(1)

        l.take_damage(5)
        self.assertTrue('dying' in l.afflictions)

    def test_take_damage_coup_de_grace(self):
        l = Lifeform()
        l.afflictions = ['dying']

        l.take_damage(5)
        self.assertTrue('dead' in l.afflictions)
