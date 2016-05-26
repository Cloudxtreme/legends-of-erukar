from erukar import *

# Inspect the room (this will occur on join)
class ExampleRunner:
    def __init__(self):
        self.interface = Interface()

        self.player = Player()
        self.player.uid = 'Bob'
        self.player.define_stats({'dexterity': 4})

        self.interface.data.players.append(PlayerNode(self.player.uid, self.player))

    def set_room(self, room):
        self.player.link_to_room(room)

    def start(self):
        print(self.interface.execute(self.player.uid, 'inspect'))
        while True:
            line = input('> ')
            print('')
            res = self.interface.execute(self.player.uid, line)
            if res is not None:
                print(res)
