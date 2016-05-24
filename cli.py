from pynarpg import *

i = Interface()

p = Player()
p.uid = 'Bob'

i.data.players.append(PlayerNode(p.uid, p))

n = Room()
n.description = 'This is the North Room.'
n_deco = Decoration(['strange cracks'], 'There are strange cracks in the floor leading into the room directly to the south.', 'These cracks appear to have been left by a blunt weapon of some sort, likely a mace.')
w = Weapon()
w.rarity, w.item_type, w.damage = ['Uncommonly Strong', 'Mace', '1d10+2']
n.add(w, 'a', 'on the floor')
n.add(n_deco, 'some', 'in the floor', plural=True)

c = Room()
c.description = 'This is the central chamber. There is a door to the south. There\'s a small opening to the north where the claw marks originate.'
c_table = Container(['small table set'], 'On the eastern side of the room is a small table set.', 'This table is made with sealed mahogony.')
c.add(c_table, 'a', 'along the eastern wall')
c_drawer = Container(['drawer'], '', 'The drawer appears to be unlocked')
c_table.add(c_drawer, 'a', 'underneath the table')
potion = Item()
potion.rarity, potion.item_type, potion.description = ['Red', 'Potion', 'This potion bottle, tiny as it is, is filled with some strange swirling red liquid. When held to the light it seems to glimmer.']
c_drawer.add(potion, 'a', 'inside')

s = Room()
s.description = 'This is the South Room.'
s_deco = Decoration(['carvings', 'etchings'], 'There are ', 'on the walls')
l = Lifeform('Gray Ooze')
l.define_level(1)
l.current_room = s
s.add(l, 'a', 'on the floor')

# Build connections between rooms
d = Door()
c.coestablish_connection(Direction.North, n, None)
c.coestablish_connection(Direction.South, s, d)
p.current_room = n

# Inspect the room (this will occur on join)
print(i.execute(p.uid, 'inspect'))
while True:
    line = input('> ')
    res = i.execute(p.uid, line)
    if res is not None:
        print(res)
