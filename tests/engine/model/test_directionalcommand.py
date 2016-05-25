from pynarpg import *
import unittest

class DirectionalCommandTests(unittest.TestCase):
    def test_determine_direction_n(self):
        m = DirectionalCommand()
        result = m.determine_direction('n')

        self.assertEqual(result, Direction.North)

    def test_determine_direction_north(self):
        m = DirectionalCommand()
        result = m.determine_direction('north')

        self.assertEqual(result, Direction.North)

    def test_determine_direction_e(self):
        m = DirectionalCommand()
        result = m.determine_direction('e')

        self.assertEqual(result, Direction.East)

    def test_determine_direction_east(self):
        m = DirectionalCommand()
        result = m.determine_direction('east')

        self.assertEqual(result, Direction.East)

    def test_determine_direction_s(self):
        m = DirectionalCommand()
        result = m.determine_direction('s')

        self.assertEqual(result, Direction.South)

    def test_determine_direction_south(self):
        m = DirectionalCommand()
        result = m.determine_direction('south')

        self.assertEqual(result, Direction.South)

    def test_determine_direction_w(self):
        m = DirectionalCommand()
        result = m.determine_direction('w')

        self.assertEqual(result, Direction.West)

    def test_determine_direction_west(self):
        m = DirectionalCommand()
        result = m.determine_direction('west')

        self.assertEqual(result, Direction.West)
