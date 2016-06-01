from erukar import *

# Inspect the room (this will occur on join)
class ExampleRunner:
    def __init__(self):
        self.interface = Interface()

        self.character = Player()
        self.character.uid = 'Bob'
        self.character.define_stats({'dexterity': 4})
        self.player = PlayerNode(self.character.uid, self.character)

        self.interface.data.players.append(self.player)

    def set_room(self, room):
        self.character.link_to_room(room)
        self.player.move_to_room(room)

    def start(self):
        print(self.interface.execute(self.character.uid, 'inspect'))
        while True:
            line = input('> ')
            print('')
            res = self.interface.execute(self.character.uid, line)
            if res is not None:
                print(res)
