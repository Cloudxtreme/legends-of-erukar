from pynarpg import *
import unittest

class AttackTests(unittest.TestCase):
    def test_execute_without_match(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        r = Room()
        p.link_to_room(r)

        a = Attack()
        a.sender_uid = p.uid
        a.data = data_store

        result = a.execute("the air")

        self.assertEqual(result, Attack.not_found.format("the air"))

    def test_execute_with_match(self):
        p = Player()
        p.uid = 'Bob'

        data_store = DataAccess()
        data_store.players.append(PlayerNode(p.uid, p))

        r = Room()
        p.link_to_room(r)

        c = Lifeform()
        c.name = "the air"
        c.link_to_room(r)

        a = Attack()
        a.sender_uid = p.uid
        a.data = data_store

        result = a.execute("the air")

        self.assertTrue("Your attack of " in result)

    def test_adjudicate_attack_success(self):
        p = Player()
        p.uid = 'Bob'
        p.weapon = Weapon()

        c = Lifeform()
        c.define_level(1)
        c.name = "the air"

        a = Armor()
        a.armor_class_modifier = -90 # guarantees success
        c.armor = a

        atk = Attack()
        result = atk.adjudicate_attack(p, c)

        self.assertTrue(' hits ' in result)

    def test_adjudicate_attack_failure(self):
        p = Player()
        p.uid = 'Bob'
        p.weapon = Weapon()

        c = Lifeform()
        c.define_level(1)
        c.name = "the air"

        a = Armor()
        a.armor_class_modifier = 90 # guarantees failure
        c.armor = a

        atk = Attack()
        result = atk.adjudicate_attack(p, c)

        self.assertTrue(' misses ' in result)

    def test_adjudicate_attack_cause_dying(self):
        p = Player()
        p.define_stats({ 'strength': 2 })
        p.uid = 'Bob'
        p.weapon = Weapon()

        c = Lifeform()
        c.health = 1
        c.name = "the air"

        a = Armor()
        a.armor_class_modifier = -90 # guarantees success
        c.armor = a

        atk = Attack()
        result = atk.adjudicate_attack(p, c)

        self.assertTrue(' has been incapacitated by your attack!' in result)
        self.assertTrue('dying' in c.afflictions)

    def test_adjudicate_attack_cause_death(self):
        r = Room()

        p = Player()
        p.define_stats({ 'strength': 2, 'dexterity': 20 })
        p.uid = 'Bob'
        p.weapon = Weapon()
        p.link_to_room(r)

        c = Lifeform()
        c.afflictions = ['dying']
        c.name = "the air"
        c.link_to_room(r)

        atk = Attack()
        result = atk.adjudicate_attack(p, c)

        self.assertTrue(' has been slain!' in result)
        self.assertTrue('dead' in c.afflictions)
        self.assertTrue(c not in r.contents)
