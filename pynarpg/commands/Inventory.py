from pynarpg.model.Command import Command

class Inventory(Command):
    def execute(self, *_):
        player = self.find_player()
        for i in range(0, len(player.inventory)):
            print("{0}.\t{1}".format(i, player.inventory[i].describe()))
