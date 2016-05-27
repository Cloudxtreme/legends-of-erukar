from erukar import *
import unittest

class DungeonGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.gen = DungeonGenerator()

    def test_connect_randomly_should_make_a_connection(self):
        r = Room()
        self.gen.connect_randomly(r, Room())

        self.assertTrue(any(r.connections[d] for d in r.connections))

    def test_connect_rooms_should_make_a_connection(self):
        rooms = [Room(), Room()]
        self.gen.connect_rooms(rooms)

        no_connections = any(rooms[0].connections[d] for d in rooms[0].connections)
        self.assertTrue(no_connections)

    def test_generate_descriptions_should_add_generic_descriptions(self):
        rooms = [Room()]
        self.gen.generate_descriptions(rooms)

        self.assertEqual(rooms[0].description, "This is the 0th room.")

    def test_fill_walls_should_not_have_abysses(self):
        rooms = [Room()]
        self.gen.fill_walls(rooms)
        r = rooms[0]

        walls = len([rooms[0].connections[d]['door'] \
            for d in rooms[0].connections if rooms[0].connections[d] is not None])
        self.assertEqual(walls, 4)

    def test_possible_directions_should_not_return_a_wall(self):
        rooms = [Room(), Room()]
        self.gen.connect_rooms(rooms)

        dirs = self.gen.possible_directions(rooms[0])
        self.assertEqual(len(dirs), 3)
