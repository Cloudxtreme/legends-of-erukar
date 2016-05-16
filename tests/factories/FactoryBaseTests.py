from pynarpg.factories.FactoryBase import FactoryBase
import unittest

class FactoryBaseTests(unittest.TestCase):
    generated_class = 'pynarpg.inventory.Weapon'

    def test_module_and_type(self):
        g = FactoryBase()
        module, ctype = g.module_and_type(FactoryBaseTests.generated_class)

        self.assertEqual(module.__name__, 'pynarpg')
        self.assertEqual(ctype, 'Weapon')

    def test_create_template(self):
        g = FactoryBase()
        result = g.create_template(FactoryBaseTests.generated_class)

        self.assertIsNotNone(result)

    def test_create_one(self):
        g = FactoryBase()
        generation_parameters = {'damage': '10d10'}
        result = g.create_one(FactoryBaseTests.generated_class, generation_parameters)

        self.assertIsNotNone(result)
        self.assertEqual(result.damage, '10d10')
