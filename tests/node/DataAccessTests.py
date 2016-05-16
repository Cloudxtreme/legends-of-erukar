from pynarpg.node.DataAccess import DataAccess
from pynarpg.model.PlayerNode import PlayerNode
import unittest

class DataAccessTests(unittest.TestCase):
    def test_find_player(self):
        d = DataAccess()
        d.players.append(PlayerNode('auid', None))

        res = d.find_player('auid')
        self.assertIsNotNone(res)

    def test_find_player_no_results(self):
        d = DataAccess()
        d.players.append(PlayerNode('audi', None))

        res = d.find_player('auid')
        self.assertIsNone(res)
