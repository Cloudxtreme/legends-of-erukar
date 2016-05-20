from pynarpg.model.Command import Command
from pynarpg.model.Direction import Direction

class DirectionalCommand(Command):
    def determine_direction(self, payload):
        '''Take text and determine its respective cardinal direction'''

        couples = [
            { "keywords": ['n', 'north'], "direction": Direction.North },
            { "keywords": ['e', 'east'], "direction": Direction.East },
            { "keywords": ['s', 'south'], "direction": Direction.South },
            { "keywords": ['w', 'west'], "direction": Direction.West } ]

        return next((x['direction'] for x in couples \
            if any([k == payload for k in x['keywords']])), None)

    def directional_description(self, direction):
        '''Turns the enumeration into North, East, South, or West'''
        pass
