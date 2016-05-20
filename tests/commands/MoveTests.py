from pynarpg.lifeforms.Player import Player
from pynarpg.model.PlayerNode import PlayerNode
from pynarpg.environment import *
from pynarpg.commands.Move import Move
from pynarpg.node.DataAccess import DataAccess
from pynarpg.model.Direction import Direction
import unittest

class MoveTests(unittest.TestCase):
    def test_execute_through_wall(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        r = Room()
        p.current_room = r

        m = Move()
        m.sender_uid = p.uid
        m.data = data_store

        result = m.execute('north')

        self.assertEqual(result, Move.move_through_wall)

    def test_execute_through_closed_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        p.current_room = n
        s = Room()
        d = Door()
        n.coestablish_connection(Direction.South, s, d)

        m = Move()
        m.sender_uid = p.uid
        m.data = data_store

        result = m.execute('south')

        self.assertEqual(result, Move.move_through_closed_door)

    def test_execute_through_open_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        p.current_room = n
        s = Room()
        d = Door()
        d.status = Door.Open
        n.coestablish_connection(Direction.South, s, d)

        m = Move()
        m.sender_uid = p.uid
        m.data = data_store

        result = m.execute('south')

        self.assertTrue('You have successfully moved South.' in result)
        self.assertEqual(p.current_room, s)
