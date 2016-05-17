from pynarpg.lifeforms.Player import Player
from pynarpg.model.PlayerNode import PlayerNode
from pynarpg.environment.Room import Room
from pynarpg.inventory import *
from pynarpg.commands.Equip import Equip
from pynarpg.node.DataAccess import DataAccess
import unittest

class EquipTests(unittest.TestCase):
    def test_equip_weapon(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        w = Weapon()
        w.item_type = 'Sword'
        p.inventory.append(w)

        e = Equip()
        e.sender_uid = p.uid
        e.data = data_store
        result = e.execute(None, 'sword')

        self.assertTrue(w in p.inventory)
        self.assertEqual(p.weapon, w)
        self.assertEqual("'Generic Sword' equipped as weapon successfully", result)

    def test_equip_armor(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        a = Armor()
        a.item_type = 'Plate Mail'
        p.inventory.append(a)

        e = Equip()
        e.sender_uid = p.uid
        e.data = data_store
        result = e.execute(None, 'plate mail')

        self.assertTrue(a in p.inventory)
        self.assertEqual(p.armor, a)
        self.assertEqual("'Generic Plate Mail' equipped as armor successfully", result)

    def test_equip_item(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        i = Item()
        i.item_type = 'Potion'
        p.inventory.append(i)

        e = Equip()
        e.sender_uid = p.uid
        e.data = data_store
        result = e.execute(None, 'potion')

        self.assertTrue(i in p.inventory)
        self.assertNotEqual(p.armor, i)
        self.assertNotEqual(p.weapon, i)
        self.assertEqual("'Generic Potion' was found but cannot be equipped", result)

    def test_equip_no_match(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        i = Item()
        i.item_type = 'Potion'
        p.inventory.append(i)

        e = Equip()
        e.sender_uid = p.uid
        e.data = data_store
        result = e.execute(None, 'sword')

        self.assertTrue(i in p.inventory)
        self.assertNotEqual(p.armor, i)
        self.assertNotEqual(p.weapon, i)
        self.assertEqual("Unable to find 'sword' in inventory", result)
