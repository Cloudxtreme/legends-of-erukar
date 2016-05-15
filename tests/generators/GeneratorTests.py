from pynarpg.generators.Generator import Generator
import unittest

class GeneratorTests(unittest.TestCase):
    def test_module_name_parsing(self):
        g = Generator('pynarpg.inventory.Armor')
        self.assertEqual('pynarpg.inventory', g.module_name)
        self.assertEqual('Armor', g.type_to_generate)

    def test_create_template(self):
        g = Generator('pynarpg.inventory.Armor')
        result = g.create_template()

        self.assertIsNotNone(result)

    def test_create_one(self):
        g = Generator('pynarpg.inventory.Armor')
        gen_params = { \
            'max_dex_mod': range(3,4), \
            'armor_class_modifier': range(3,4)}
        result = g.create_one(gen_params)

        self.assertIsNotNone(result)
        self.assertTrue(result.armor_class_modifier > 2)
        self.assertTrue(result.max_dex_mod > 2)

    def test_generate(self):
        g = Generator('pynarpg.inventory.Armor')
        gen_params = { \
            'max_dex_mod': range(3,4), \
            'armor_class_modifier': range(3,4)}

        result = g.generate(10, gen_params)
        self.assertEqual(10, len(result))
