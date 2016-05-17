from pynarpg.environment.Room import Room
import unittest

class RoomTests(unittest.TestCase):
    def test_invert_direction_from_north(self):
        room = Room()
        result = room.invert_direction(Room.North)

        self.assertEqual(Room.South, result)

    def test_invert_direction_from_east(self):
        room = Room()
        result = room.invert_direction(Room.East)

        self.assertEqual(Room.West, result)

    def test_invert_direction_from_south(self):
        room = Room()
        result = room.invert_direction(Room.South)

        self.assertEqual(Room.North, result)

    def test_invert_direction_from_west(self):
        room = Room()
        result = room.invert_direction(Room.West)

        self.assertEqual(Room.East, result)

    def test_connect_room(self):
        n = Room()
        s = Room()

        n.connect_room(Room.South, s, None)
        s.connect_room(Room.North, n, None)

        n_result = n.get_in_direction(Room.South)
        s_result = s.get_in_direction(Room.North)

        self.assertEqual(n_result['room'], s)
        self.assertEqual(s_result['room'], n)
        self.assertIsNone(n_result['door'])
        self.assertIsNone(s_result['door'])

    def test_coestablish_connection(self):
        n = Room()
        s = Room()

        n.coestablish_connection(Room.South, s, None)

        n_result = n.get_in_direction(Room.South)
        s_result = s.get_in_direction(Room.North)

        self.assertEqual(n_result['room'], s)
        self.assertEqual(s_result['room'], n)
        self.assertIsNone(n_result['door'])
        self.assertIsNone(s_result['door'])
