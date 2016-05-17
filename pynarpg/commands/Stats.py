from pynarpg.model.Command import Command

class Stats(Command):
    def execute(self, *_):
        player = self.find_player()
        for stat in ['str', 'dex', 'vit']:
            print("{0}\t{1}".format(stat.upper(), player.attributes[stat]))
