from erukar.engine.commands.Inspect import Inspect
from erukar.engine.model.Command import Command
from erukar.engine.environment import *

class Map(Command):
    def execute(self, payload):
        '''Converts the dungeon_map into a readable map for the user'''
        player = self.find_player()
        room = player.character.current_room

        max_x, max_y = map(max, zip(*player.dungeon_map))
        min_x, min_y = map(min, zip(*player.dungeon_map))

        # Adjust these such that we account for the borders
        dnjn_map = [['□' if (x,y) in player.dungeon_map else '■'
            for x in range(min_x-1, max_x+2)] for y in range(min_y-1, max_y+2)]

        # show the player as an X
        dnjn_map[1+room.coordinates[1] - min_y][1+room.coordinates[0] - min_x] = 'X'
        return '\n'.join(' '.join(y) for y in reversed(dnjn_map))
