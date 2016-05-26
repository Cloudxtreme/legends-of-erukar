from erukar import *
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
        result = e.execute('sword')

        self.assertTrue(w in p.inventory)
        self.assertEqual(p.weapon, w)
        self.assertEqual(Equip.equipped_weapon.format('Generic Sword'), result)

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
        result = e.execute('plate mail')

        self.assertTrue(a in p.inventory)
        self.assertEqual(p.armor, a)
        self.assertEqual(Equip.equipped_armor.format('Generic Plate Mail'), result)

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
        result = e.execute('potion')

        self.assertTrue(i in p.inventory)
        self.assertNotEqual(p.armor, i)
        self.assertNotEqual(p.weapon, i)
        self.assertEqual(Equip.cannot_equip.format('Generic Potion'), result)

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
        result = e.execute('sword')

        self.assertTrue(i in p.inventory)
        self.assertNotEqual(p.armor, i)
        self.assertNotEqual(p.weapon, i)
        self.assertEqual(Equip.not_found.format('sword'), result)


    def test_item_type(self):
        w = Weapon()
        e = Equip()
        result = e.item_type(w)
        self.assertEqual(result, 'weapon')
