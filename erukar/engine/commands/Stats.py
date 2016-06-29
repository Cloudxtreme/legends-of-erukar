from erukar.engine.model import Command
from erukar.engine.lifeforms import Lifeform

class Stats(Command):
    header = 'STATS\n----------\n'
    stat = "{0:10} {1}"

    def execute(self, *_):
        player = self.find_player()
        stats = '\n'.join([Stats.stat.format(stat.capitalize(), player.character.get(stat)) \
            for stat in Lifeform.attribute_types])

        return Stats.header + stats + '\n'
