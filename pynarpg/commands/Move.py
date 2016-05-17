from pynarpg.model.Command import Command
from pynarpg.environment.Room import Room

class Move(Command):

    def execute(self, room, payload):
        player = self.find_player()
        direction = self.determine_direction(payload.lower())

    def determine_direction(self, payload):
        '''Take text and determine its respective cardinal direction'''

        couples = [
            { "keywords": ['n', 'north'], "direction": Room.North },
            { "keywords": ['e', 'east'], "direction": Room.East },
            { "keywords": ['s', 'south'], "direction": Room.South },
            { "keywords": ['w', 'west'], "direction": Room.West } ]

        return next((x['direction'] for x in couples \
            if any([k == payload for k in x['keywords']])), None)
