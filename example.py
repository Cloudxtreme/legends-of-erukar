from erukar import *

i = Interface()

p = Player()
p.uid = 'Bob'
p.define_stats({'dexterity': 4})

i.data.players.append(PlayerNode(p.uid, p))

# North Room
n = Room()
n.description = 'This is the North Room.'
n_deco = Decoration(aliases=['strange cracks'], description='There are strange cracks in the floor leading into the room directly to the south.', inspect_results='These cracks appear to have been left by a blunt weapon of some sort, likely a mace.')
w = Weapon()
w.rarity, w.item_type, w.damage = ['Uncommonly Strong', 'Mace', '1d10+2']
n.add(article='a', item=w, preposition='on the floor')
n.add(article='some', item=n_deco, preposition='in the floor', plural=True)

# Central Room
c = Room()
c.description = 'This is the central chamber. There is a door to the south. There\'s a small opening to the north where the claw marks originate.'
c_table = Container(aliases=['small table set'], description='On the eastern side of the room is a small table set.', inspect_results='This table is made with sealed mahogony.')
c.add(article='a', item=c_table, preposition='along the eastern wall')
c_drawer = Container(aliases=['drawer'], description='The drawer appears to be unlocked.', inspect_results='The drawer appears to be unlocked.')
c_table.add(article='a', item=c_drawer, preposition='underneath the table')
potion = Item()
potion.rarity, potion.item_type, potion.description = ['Red', 'Potion', 'This potion bottle, tiny as it is, is filled with some strange swirling red liquid. When held to the light it seems to glimmer.']
c_drawer.add(article='a', item=potion, preposition='inside')

# South Room
s = Room()
s.description = 'This is the South Room.'
s_deco = Decoration(aliases=['carvings', 'etchings'], description='There are ', inspect_results='on the walls')
l = Lifeform('Gray Ooze')
l.define_level(1)
l.current_room = s
s.add(article='a', item=l, preposition='on the floor')

# Build connections between rooms
d = Door()
c.coestablish_connection(Direction.North, n, None)
c.coestablish_connection(Direction.South, s, d)
p.current_room = n

# Inspect the room (this will occur on join)
print(i.execute(p.uid, 'inspect'))
while True:
    line = input('> ')
    print('')
    res = i.execute(p.uid, line)
    if res is not None:
        print(res)
