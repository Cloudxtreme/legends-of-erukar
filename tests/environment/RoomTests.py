from pynarpg.environment.Room import Room
import unittest

class RoomTests(unittest.TestCase):
    def test_invert_direction(self):
        room = Room()
        result = room.invert_direction(Room.South)

        self.assertEqual(Room.North, result)
