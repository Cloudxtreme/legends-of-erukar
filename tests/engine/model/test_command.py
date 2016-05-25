from pynarpg import *
import unittest

class CommandTests(unittest.TestCase):
    def test_find_player(self):
        c = Command()
        c.sender_uid = 'auid'

        d = DataAccess()
        d.players.append(PlayerNode('auid', None))
        c.data = d

        result = c.find_player()

        self.assertEqual(result.uid, 'auid')

    def test_find_in_room(self):
        c = Command()
        c.sender_uid = 'auid'
        w = Weapon()
        r = Room()
        r.contents.append(w)

        d = DataAccess()
        d.players.append(PlayerNode('auid', None))
        c.data = d

        result = c.find_in_room(r, w.item_type)

        self.assertEqual(w, result)

    def test_find_in_inventory(self):
        c = Command()
        p = Player()
        w = Weapon()

        p.uid = 'Bob'
        p.inventory.append(w)
        n = PlayerNode(p.uid, p)

        result = c.find_in_inventory(n, w.item_type)

        self.assertEqual(w, result)
