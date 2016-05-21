from pynarpg import *

i = Interface()

p = Player()
p.uid = 'Bob'

i.data.players.append(PlayerNode(p.uid, p))

n = Room()
n.description = 'This is the North Room. There are strange cracks in the floor leading into the room directly to the south.'
n_deco = Decoration(['gashes', 'cuts', 'scratches'], 'These cracks appear to have been left by a blunt weapon of some sort.')
n.add(n_deco)

c = Room()
c.description = 'This is the central chamber. There is a small table set. There\'s a small opening to the north where the claw marks originate and a door to the south.'
c_deco = Decoration(['small table set'], 'On the table is a potion filled with a red liquid. There\'s nothing more of note about it, however.')
potion = Item('Potion')
potion.rarity = 'Red'
potion.description = 'This potion bottle, tiny as it is, is filled with some strange swirling red liquid. When held to the light it seems to glimmer.'
c.add(c_deco)
c.add(potion)

s = Room()
s.description = 'This is the South Room. There\'s nothing really interesting in this room.'

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
