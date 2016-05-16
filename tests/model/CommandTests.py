from pynarpg.model.Command import Command
from pynarpg.model.PlayerNode import PlayerNode
from pynarpg.node.DataAccess import DataAccess
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
