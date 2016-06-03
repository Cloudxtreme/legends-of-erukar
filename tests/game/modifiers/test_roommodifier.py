from erukar import *
import unittest

class RoomModifierTests(unittest.TestCase):
    def test_apply_to_room_actually_applies(self):
        r = Room()
        mod = RoomModifier()
        mod.modify(r)

        self.assertEqual(r.description, ' The air is dusty.')
