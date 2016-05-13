from pynarpg.lifeforms.player import Player
from pynarpg.inventory.armor import Armor
import unittest

class PlayerTests(unittest.TestCase):
    def test_calculate_armor_class_no_armor(self):
        p = Player()
        p.define_stats(dexterity=2)
        ac = p.calculate_armor_class()

        self.assertEqual(10, ac)

    def test_calculate_armor_class_with_armor(self):
        p = Player()
        p.define_stats(dexterity=2)

        test_armor = Armor()
        test_armor.armor_class = 12
        test_armor.max_dex_mod = 2
        p.armor = test_armor

        ac = p.calculate_armor_class()
        self.assertEqual(12, ac)

    def test_skill_roll_string_positive_mod(self):
        p = Player()
        p.define_stats(dexterity=2)
        dex_srs = p.skill_roll_string('dex')
        self.assertEqual('1d20+2', dex_srs)


    def test_skill_roll_string_negative_mod(self):
        p = Player()
        p.define_stats()
        dex_srs = p.skill_roll_string('dex')
        self.assertEqual('1d20-2', dex_srs)
