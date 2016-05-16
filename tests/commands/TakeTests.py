from pynarpg.lifeforms.Player import Player
from pynarpg.model.PlayerNode import PlayerNode
from pynarpg.environment.Room import Room
from pynarpg.inventory.Weapon import Weapon
from pynarpg.commands.Take import Take
from pynarpg.node.DataAccess import DataAccess
import unittest

class TakeTests(unittest.TestCase):
    def test_take_execution(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        w = Weapon()
        r = Room()
        r.contents.append(w)

        t = Take()
        t.sender_uid = p.uid
        t.data = data_store
        t.execute(r, w.item_type)

        self.assertTrue(w in p.inventory)
        self.assertTrue(w not in r.contents)
