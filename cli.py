from pynarpg import *

i = Interface()

p = Player()
p.uid = 'Bob'

i.data.players.append(PlayerNode(p.uid, p))

n = Room()
n.description = 'This is the North Room. There are strange claw marks on the floor leading into the room directly to the south.'
n_deco = Decoration(['claw marks', 'scratches'], 'The claw marks appear to have been left by some sort of large creature')
n.add(n_deco)

c = Room()
c.description = 'This is the central chamber. There is a small table set. There\'s a small opening to the north where the claw marks originate and a door to the south.'
c_deco = Decoration(['table set'], 'On the table is a potion filled with a red liquid. There\'s nothing more of note about it, however.')
potion = Item('Potion')
potion.rarity = 'Red'
c.add(c_deco)
c.add(potion)

s = Room()
s.description = 'This is the South Room. There\'s nothing really interesting in this room.'

d = Door()
c.coestablish_connection(Direction.North, n, None)
c.coestablish_connection(Direction.South, s, d)
p.current_room = n

while True:
    line = input('> ')
    res = i.execute(p.uid, line)
    print(res)
