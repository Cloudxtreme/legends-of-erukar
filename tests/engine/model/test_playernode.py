from erukar import *
import unittest

class PlayerNodeTests(unittest.TestCase):
    def test_index_item_no_container_yet(self):
        p = PlayerNode('', None)
        i = Item()
        r = Room()

        p.index_item(i, r)

        self.assertTrue(r in p.item_indexer)
        self.assertTrue(i in p.item_indexer)
        self.assertEqual(p.item_indexer[r], [])
        self.assertEqual(p.item_indexer[i], [r])

    def test_index_item_with_nested_container(self):
        p = PlayerNode('', None)
        r = Room()
        c = Container([],'','')
        r.add(c)
        i = Item()
        c.add(i)

        p.index_item(c, r)
        p.index_item(i, c)

        self.assertTrue(r in p.item_indexer)
        self.assertTrue(c in p.item_indexer)
        self.assertTrue(i in p.item_indexer)
        self.assertEqual(p.item_indexer[r], [])
        self.assertEqual(p.item_indexer[c], [r])
        self.assertEqual(p.item_indexer[i], [r, c])

    def test_index_with_match(self):
        p = PlayerNode('', None)
        r = Room()
        c = Container([],'','')
        r.add(c)
        i = Item()
        c.add(i)

        p.index_item(c, r)
        p.index_item(i, c)

        result = p.index(i)

        self.assertEqual(result, [r, c])

    def test_index_without_match(self):
        p = PlayerNode('', None)
        r = Room()
        c = Container([],'','')
        r.add(c)
        i = Item()
        c.add(i)

        p.index_item(c, r)

        result = p.index(i)

        self.assertEqual(result, [])

    def test_reverse_index(self):
        p = PlayerNode('', None)
        r = Room()
        c = Container([],'','')
        r.add(c)
        i = Item()
        c.add(i)

        p.index_item(c, r)
        p.index_item(i, c)

        c_result = p.reverse_index(c)
        r_result = p.reverse_index(r)

        self.assertEqual(c_result, [i])
        self.assertEqual(set(r_result), {c, i})
