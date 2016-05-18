from pynarpg.lifeforms.Player import Player
from pynarpg.model.PlayerNode import PlayerNode
from pynarpg.environment.Room import Room
from pynarpg.inventory import *
from pynarpg.commands.Unequip import Unequip
from pynarpg.node.DataAccess import DataAccess
import unittest

class UnequipTests(unittest.TestCase):
    def test_unequip_weapon(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        w = Weapon()
        w.item_type = 'Sword'
        p.inventory.append(w)
        p.weapon = w;

        u = Unequip()
        u.sender_uid = p.uid
        u.data = data_store
        result = u.execute('sword')

        self.assertTrue(w in p.inventory)
        self.assertEqual(p.weapon, None)
        self.assertEqual(Unequip.unequipped_weapon, result)

    def test_unequip_armor(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        a = Armor()
        a.item_type = 'Plate Mail'
        p.inventory.append(a)
        p.armor = a;

        u = Unequip()
        u.sender_uid = p.uid
        u.data = data_store
        result = u.execute('plate mail')

        self.assertTrue(a in p.inventory)
        self.assertEqual(p.armor, None)
        self.assertEqual(Unequip.unequipped_armor, result)

    def test_unequip_item(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        i = Item()
        i.item_type = 'Potion'
        p.inventory.append(i)

        u = Unequip()
        u.sender_uid = p.uid
        u.data = data_store
        result = u.execute('potion')

        self.assertTrue(i in p.inventory)
        self.assertEqual(Unequip.not_found.format('potion'), result)
