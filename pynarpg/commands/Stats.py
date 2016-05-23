from pynarpg import Command, Lifeform

class Stats(Command):
    def execute(self, *_):
        player = self.find_player()
        for stat in Lifeform.attribute_types:
            print("{0}\t{1}".format(stat.capitalize(), player.character.get(stat)))
