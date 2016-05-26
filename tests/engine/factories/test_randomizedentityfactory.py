from erukar import *
import unittest

class RandomizedEntityFactoryTests(unittest.TestCase):
    generated_class = 'erukar.engine.inventory.Armor'

    def test_create_template(self):
        g = RandomizedEntityFactory()
        result = g.create_template(RandomizedEntityFactoryTests.generated_class)

        self.assertIsNotNone(result)

    def test_create_one(self):
        g = RandomizedEntityFactory()
        gen_params = { \
            'max_dex_mod': range(3,4), \
            'armor_class_modifier': range(3,4)}
        result = g.create_one(RandomizedEntityFactoryTests.generated_class, gen_params)

        self.assertIsNotNone(result)
        self.assertTrue(result.armor_class_modifier > 2)
        self.assertTrue(result.max_dex_mod > 2)

    def test_generate(self):
        g = RandomizedEntityFactory()
        gen_params = { \
            'max_dex_mod': range(3,4), \
            'armor_class_modifier': range(3,4)}

        result = g.generate(RandomizedEntityFactoryTests.generated_class, 10, gen_params)
        self.assertEqual(10, len(result))
