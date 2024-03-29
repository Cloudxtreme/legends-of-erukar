from erukar import *
import unittest

class OpenTests(unittest.TestCase):
    def test_execute_through_wall(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        r = Room()
        p.current_room = r

        o = Open()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('north')

        self.assertEqual(result, Open.nesw_no_door)

    def test_execute_through_no_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        p.current_room = n
        s = Room()
        n.coestablish_connection(Direction.South, s, None)

        o = Open()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('south')

        self.assertEqual(result, Open.nesw_no_door)

    def test_execute_through_locked_door(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        p.current_room = n
        s = Room()
        d = Door()
        d.status = Door.Locked
        n.coestablish_connection(Direction.South, s, d)

        o = Open()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('south')

        self.assertEqual(result, Open.nesw_locked)

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

        o = Open()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('south')

        self.assertEqual(result, Open.nesw_already_open)

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

        o = Open()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('south')

        self.assertEqual(result, Open.nesw_open_success)
        self.assertEqual(d.status, Door.Open)

    def test_execute_on_chest(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        n = Room()
        p.current_room = n
        chest = Container(aliases=['chest'], inspect_results='', broad_results='')
        n.add(chest)

        o = Open()
        o.sender_uid = p.uid
        o.data = data_store

        result = o.execute('chest')

        self.assertEqual(result, 'Opened a chest')
