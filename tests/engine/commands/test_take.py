from erukar import *
import unittest

class TakeTests(unittest.TestCase):
    def test_take_execution(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        w = Weapon()
        w.item_type = 'Sword'
        r = Room()
        p.current_room = r
        r.add(article='a', item=w, preposition='on the floor')

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