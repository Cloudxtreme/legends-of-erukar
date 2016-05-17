from pynarpg.model.DirectionalCommand import DirectionalCommand
from pynarpg.environment.Room import Room
import unittest

class DirectionalCommandTests(unittest.TestCase):
    def test_determine_direction_n(self):
        m = DirectionalCommand()
        result = m.determine_direction('n')

        self.assertEqual(result, Room.North)

    def test_determine_direction_north(self):
        m = DirectionalCommand()
        result = m.determine_direction('north')

        self.assertEqual(result, Room.North)

    def test_determine_direction_e(self):
        m = DirectionalCommand()
        result = m.determine_direction('e')

        self.assertEqual(result, Room.East)

    def test_determine_direction_east(self):
        m = DirectionalCommand()
        result = m.determine_direction('east')

        self.assertEqual(result, Room.East)

    def test_determine_direction_s(self):
        m = DirectionalCommand()
        result = m.determine_direction('s')

        self.assertEqual(result, Room.South)

    def test_determine_direction_south(self):
        m = DirectionalCommand()
        result = m.determine_direction('south')

        self.assertEqual(result, Room.South)

    def test_determine_direction_w(self):
        m = DirectionalCommand()
        result = m.determine_direction('w')

        self.assertEqual(result, Room.West)

    def test_determine_direction_west(self):
        m = DirectionalCommand()
        result = m.determine_direction('west')

        self.assertEqual(result, Room.West)
