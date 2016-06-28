from erukar import *
import unittest

class TakeTests(unittest.TestCase):
    def test_take_execution(self):
        p = Player()
        p.uid = 'Bob'

        pn = PlayerNode(p.uid, p)
        data_store = DataAccess()
        data_store.players.append(pn)

        w = Weapon()
        w.item_type = 'Sword'
        r = Room()
        r.add(w)
        p.link_to_room(r)
        pn.move_to_room(r)

        # Inspect the room to index the item
        i = Inspect()
        i.sender_uid = p.uid
        i.data = data_store
        i.execute('')

        # Now take it
        t = Take()
        t.sender_uid = p.uid
        t.data = data_store
        result = t.execute('sword')

        self.assertTrue(w in p.inventory)
        self.assertTrue(w not in r.contents)
        self.assertEqual(result, Take.success.format('Generic Sword'))

    def test_take_execution_no_match(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        w = Weapon()
        w.item_type = 'Firearm'
        r = Room()
        p.current_room = r
        r.contents.append(w)

        t = Take()
        t.sender_uid = p.uid
        t.data = data_store
        result = t.execute('Sword')

        self.assertTrue(w in r.contents)
        self.assertTrue(w not in p.inventory)
        self.assertEqual(result, Take.failure.format('Sword'))
