from pynarpg.generators.Generator import Generator
import unittest

class GeneratorTests(unittest.TestCase):
    def test_module_name_parsing(self):
        g = Generator('pynarpg.inventory.Armor')
        self.assertEqual('pynarpg.inventory', g.module_name)
        self.assertEqual('Armor', g.type_to_generate)

    def test_create_one(self):
        g = Generator('pynarpg.inventory.Armor')
        result = g.create_one()

        self.assertIsNotNone(result)
