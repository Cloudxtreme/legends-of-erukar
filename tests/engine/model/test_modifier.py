from erukar import *
import unittest

class ModifierTests(unittest.TestCase):
    def test_can_apply_to_is_false_when_NONE(self):
        m = Modifier()
        m.permission_type = Modifier.NONE

        w = Weapon()
        result = m.can_apply_to(w)

        self.assertEqual(result, False)

    def test_can_apply_to_is_true_when_ALL(self):
        m = Modifier()
        m.permission_type = Modifier.ALL

        w = Weapon()
        result = m.can_apply_to(w)

        self.assertEqual(result, True)

    def test_can_apply_to_is_true_when_ALL_PERMITTED_and_in_permitted(self):
        m = Modifier()
        m.permission_type = Modifier.ALL_PERMITTED
        m.permitted_entities.append(Weapon)

        w = Weapon()
        result = m.can_apply_to(w)

        self.assertEqual(result, True)

    def test_can_apply_to_is_false_when_ALL_PERMITTED_and_not_in_permitted(self):
        m = Modifier()
        m.permission_type = Modifier.ALL_PERMITTED

        w = Weapon()
        result = m.can_apply_to(w)

        self.assertEqual(result, False)

    def test_can_apply_to_is_true_when_NONE_PROHIBITED_and_not_in_prohibited(self):
        m = Modifier()
        m.permission_type = Modifier.NONE_PROHIBITED

        w = Weapon()
        result = m.can_apply_to(w)

        self.assertEqual(result, True)

    def test_can_apply_to_is_false_when_NONE_PROHIBITED_and_in_prohibited(self):
        m = Modifier()
        m.permission_type = Modifier.NONE_PROHIBITED
        m.prohibited_entities.append(Weapon)

        w = Weapon()
        result = m.can_apply_to(w)

        self.assertEqual(result, False)

    def test_is_in_group_works_if_subclass(self):
        m = Modifier()
        w = Weapon()
        result = m.is_in_group(w, [Item])

        self.assertEqual(result, True)
