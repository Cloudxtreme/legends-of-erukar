from erukar.engine.model import Command
from erukar.engine.lifeforms import Lifeform

class Stats(Command):
    def execute(self, *_):
        player = self.find_player()
        return '\n'.join(["{0:10}{1}".format(stat.capitalize(), player.character.get(stat)) \
            for stat in Lifeform.attribute_types])
