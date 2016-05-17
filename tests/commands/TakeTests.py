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
        w.item_type = 'Sword'
        r = Room()
        r.contents.append(w)

        t = Take()
        t.sender_uid = p.uid
        t.data = data_store
        t.execute(r, 'sword')

        self.assertTrue(w in p.inventory)
        self.assertTrue(w not in r.contents)

    def test_take_execution_no_match(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        w = Weapon()
        w.item_type = 'Firearm'
        r = Room()
        r.contents.append(w)

        t = Take()
        t.sender_uid = p.uid
        t.data = data_store
        t.execute(r, 'Sword')

        self.assertTrue(w in r.contents)
        self.assertTrue(w not in p.inventory)
