from erukar import *
import unittest

class CloseTests(unittest.TestCase):
    def test_execute_through_wall(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        r = Room()
        p.current_room = r

        o = Close()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('north')

        self.assertEqual(result, Close.nesw_no_door)

    def test_execute_through_no_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        p.current_room = n
        s = Room()
        n.coestablish_connection(Direction.South, s, None)

        o = Close()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('south')

        self.assertEqual(result, Close.nesw_no_door)

    def test_execute_through_locked_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        s = Room()
        d = Door()
        p.current_room = n
        d.status = Door.Locked
        n.coestablish_connection(Direction.South, s, d)

        o = Close()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('south')

        self.assertEqual(result, Door.already_closed)

    def test_execute_through_closed_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        s = Room()
        p.current_room = n
        d = Door()
        n.coestablish_connection(Direction.South, s, d)

        o = Close()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('south')
        self.assertEqual(result, Door.already_closed)


    def test_execute_through_open_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        s = Room()
        d = Door()
        p.current_room = n
        d.status = Door.Open
        n.coestablish_connection(Direction.South, s, d)

        o = Close()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('south')

        self.assertEqual(result, Door.close_success)
        self.assertEqual(d.status, Door.Closed)

    def test_execute_on_chest(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        p.current_room = n
        chest = Container(aliases=['chest'], inspect_results='', broad_results='')
        n.add(item=chest)

        o = Close()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('chest')

        self.assertEqual(result, 'Closed a chest')
