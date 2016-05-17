from pynarpg.lifeforms.Player import Player
from pynarpg.model.PlayerNode import PlayerNode
from pynarpg.environment import *
from pynarpg.commands.Move import Move
from pynarpg.node.DataAccess import DataAccess
import unittest

class MoveTests(unittest.TestCase):
    def test_execute_through_wall(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        r = Room()

        m = Move()
        m.sender_uid = p.uid
        m.data = data_store

        result = m.execute(r, 'north')

        self.assertEqual(result, Move.move_through_wall)

    def test_execute_through_closed_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        s = Room()
        d = Door()
        n.coestablish_connection(Room.South, s, d)

        m = Move()
        m.sender_uid = p.uid
        m.data = data_store

        result = m.execute(n, 'south')

        self.assertEqual(result, Move.move_through_closed_door)

    def test_execute_through_closed_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        s = Room()
        d = Door()
        d.status = Door.Open
        n.coestablish_connection(Room.South, s, d)

        m = Move()
        m.sender_uid = p.uid
        m.data = data_store

        result = m.execute(n, 'south')

        self.assertEqual(result, Move.move_successful)
        self.assertEqual(p.current_room, s)

    def test_determine_direction_n(self):
        m = Move()
        result = m.determine_direction('n')

        self.assertEqual(result, Room.North)

    def test_determine_direction_north(self):
        m = Move()
        result = m.determine_direction('north')

        self.assertEqual(result, Room.North)

    def test_determine_direction_e(self):
        m = Move()
        result = m.determine_direction('e')

        self.assertEqual(result, Room.East)

    def test_determine_direction_east(self):
        m = Move()
        result = m.determine_direction('east')

        self.assertEqual(result, Room.East)

    def test_determine_direction_s(self):
        m = Move()
        result = m.determine_direction('s')

        self.assertEqual(result, Room.South)

    def test_determine_direction_south(self):
        m = Move()
        result = m.determine_direction('south')

        self.assertEqual(result, Room.South)

    def test_determine_direction_w(self):
        m = Move()
        result = m.determine_direction('w')

        self.assertEqual(result, Room.West)

    def test_determine_direction_west(self):
        m = Move()
        result = m.determine_direction('west')

        self.assertEqual(result, Room.West)
