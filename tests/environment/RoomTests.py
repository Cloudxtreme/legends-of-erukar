from pynarpg.environment.Room import Room
from pynarpg.model.Direction import Direction
import unittest

class RoomTests(unittest.TestCase):
    def test_invert_direction_from_north(self):
        room = Room()
        result = room.invert_direction(Direction.North)

        self.assertEqual(Direction.South, result)

    def test_invert_direction_from_east(self):
        room = Room()
        result = room.invert_direction(Direction.East)

        self.assertEqual(Direction.West, result)

    def test_invert_direction_from_south(self):
        room = Room()
        result = room.invert_direction(Direction.South)

        self.assertEqual(Direction.North, result)

    def test_invert_direction_from_west(self):
        room = Room()
        result = room.invert_direction(Direction.West)

        self.assertEqual(Direction.East, result)

    def test_connect_room(self):
        n = Room()
        s = Room()

        n.connect_room(Direction.South, s, None)
        s.connect_room(Direction.North, n, None)

        n_result = n.get_in_direction(Direction.South)
        s_result = s.get_in_direction(Direction.North)

        self.assertEqual(n_result['room'], s)
        self.assertEqual(s_result['room'], n)
        self.assertIsNone(n_result['door'])
        self.assertIsNone(s_result['door'])

    def test_coestablish_connection(self):
        n = Room()
        s = Room()

        n.coestablish_connection(Direction.South, s, None)

        n_result = n.get_in_direction(Direction.South)
        s_result = s.get_in_direction(Direction.North)

        self.assertEqual(n_result['room'], s)
        self.assertEqual(s_result['room'], n)
        self.assertIsNone(n_result['door'])
        self.assertIsNone(s_result['door'])
