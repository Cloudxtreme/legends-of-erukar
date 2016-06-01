from erukar import *
from examples.helpers.ExampleRunner import ExampleRunner

runner = ExampleRunner()

# North Room
n = Room((0,0))
n.description = 'This room is cold and dusty.'
n_deco = Decoration(aliases=['strange cracks'], inspect_results='These cracks appear to have been left by a blunt weapon of some sort, likely a mace.')
w = Weapon()
w.rarity, w.item_type, w.damage = ['Uncommonly Strong', 'Mace', '1d10+2']
n.add(article='a', item=w, preposition='on the floor')
n.add(article='some', item=n_deco, preposition='in the floor', plural=True)

# Central Room
c = Room((0,-1))
c.description = 'This is the central chamber.'
c_table = Container(aliases=['small table set'], inspect_results='This table is made with sealed mahogony.')
c.add(article='a', item=c_table, preposition='along the eastern wall')
c_drawer = Container(aliases=['drawer'], inspect_results='The drawer appears to be unlocked.')
c_table.add(article='a', item=c_drawer, preposition='underneath the table')
potion = Item()
potion.rarity, potion.item_type, potion.description = ['Red', 'Potion', 'This potion bottle, tiny as it is, is filled with some strange swirling red liquid. When held to the light it seems to glimmer.']
c_drawer.add(article='a', item=potion, preposition='inside')

# South Room
s = Room((0,-2))
s.description = 'This is the southern-most room in the dungeon.'
s_deco = Decoration(aliases=['carvings', 'etchings'], inspect_results='on the walls')
l = Lifeform('Gray Ooze')
l.define_level(1)
l.current_room = s
s.add(article='a', item=l, preposition='on the floor')

# Build connections between rooms
d = Door()
c.coestablish_connection(Direction.North, n, None)
c.coestablish_connection(Direction.South, s, d)
runner.set_room(n)

runner.start()
