from pynarpg.commands.Move import Move
from pynarpg.environment.Room import Room
import unittest

class MoveTests(unittest.TestCase):
    def test_determine_direction_n(self):
        m = Move()
        result = m.determine_direction('n')

        self.assertTrue(result, Room.North)

    def test_determine_direction_north(self):
        m = Move()
        result = m.determine_direction('north')

        self.assertTrue(result, Room.North)

    def test_determine_direction_e(self):
        m = Move()
        result = m.determine_direction('e')

        self.assertTrue(result, Room.North)

    def test_determine_direction_east(self):
        m = Move()
        result = m.determine_direction('east')

        self.assertTrue(result, Room.East)

    def test_determine_direction_s(self):
        m = Move()
        result = m.determine_direction('s')

        self.assertTrue(result, Room.South)

    def test_determine_direction_south(self):
        m = Move()
        result = m.determine_direction('south')

        self.assertTrue(result, Room.South)

    def test_determine_direction_w(self):
        m = Move()
        result = m.determine_direction('w')

        self.assertTrue(result, Room.West)

    def test_determine_direction_west(self):
        m = Move()
        result = m.determine_direction('west')

        self.assertTrue(result, Room.West)
