from erukar import *
import unittest

class MoveTests(unittest.TestCase):
    def test_change_room(self):
        c = Player()
        c.uid = 'Bob'

        p = PlayerNode(c.uid, c)
        data_store = DataAccess()
        data_store.players.append(p)

        old_room = Room()
        c.current_room = old_room
        new_room = Room()
        new_room.description = 'new_room'

        m = Move()
        m.data = data_store
        m.sender_uid = c.uid
        result = m.change_room(p, new_room, Direction.South)

        self.assertEqual(result, Move.move_successful.format('South', 'new_room') +' \n')
        self.assertTrue(c in new_room.contents)
        self.assertTrue(c not in old_room.contents)

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
