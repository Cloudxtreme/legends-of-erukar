from erukar import *
from examples.helpers.ExampleRunner import ExampleRunner

runner = ExampleRunner()
dungeon_generator = DungeonGenerator()

# North Room
n = Room((0,0))
n.description = 'This room is cold and dusty.'
n_deco = Decoration(aliases=['strange cracks'], \
    broad_results="The floor contains several strain cracks.",\
    inspect_results='These cracks appear to have been left by a blunt weapon of some sort, likely a mace.')
w = Weapon()
w.rarity, w.item_type, w.damage = ['Uncommonly Strong', 'Mace', '1d10+2']
n.add(w)
n.add(n_deco)

# Central Room
c = Room((0,-1))
c.description = 'This is the central chamber.'
c_table = Container(aliases=['small table set'], \
    broad_results=" ", \
    inspect_results='This table is made with sealed mahogony.')
c.add(c_table)
c_drawer = Container(aliases=['drawer'], \
    broad_results="There is a drawer",
    inspect_results='The drawer appears to be unlocked.')
c_table.add(c_drawer)
potion = Item()
potion.rarity, potion.item_type, potion.description = ['Red', 'Potion', 'This potion bottle, tiny as it is, is filled with some strange swirling red liquid. When held to the light it seems to glimmer.']
c_drawer.add(potion)

# South Room
s = Room((0,-2))
s.description = 'This is the southern-most room in the dungeon.'
s_deco = Decoration(aliases=['carvings', 'etchings'], \
    broad_results='There are several ornamental carvings and etchings on the walls', \
    inspect_results="These carvings are some form of ancient heiroglyphics. Nowadays, it might be better described as art.")
l = Lifeform('Gray Ooze')
l.define_level(1)
l.current_room = s
s.add(l)

# Build connections between rooms
d = Door()
c.coestablish_connection(Direction.North, n, None)
c.coestablish_connection(Direction.South, s, d)

dungeon_generator.dungeon = Dungeon()
dungeon_generator.dungeon.rooms = [n, c, s]
dungeon_generator.fill_walls()
runner.set_room(n)

runner.start()
