from pynarpg.model.EnvironmentPiece import EnvironmentPiece
from pynarpg.model.Direction import Direction

class Room(EnvironmentPiece):

    def __init__(self):
        self.contents = []
        self.connections = {direction: None for direction in Direction}
        self.nesw_descriptions = {direction: 'TBD' for direction in Direction}
        self.description = ''

    def connect_room(self, direction, other_room, door=None):
        self.connections[direction] = { "room": other_room, "door": door}

    def add(self, item):
        self.contents.append(item)

    def invert_direction(self, direction):
        return Direction( (direction.value + 2) % 4 )

    def get_in_direction(self, direction):
        return self.connections[direction]

    def coestablish_connection(self, direction, other_room, door=None):
        '''Establishes a connection to both rooms'''
        self.connect_room(direction, other_room, door)
        other_room.connect_room(self.invert_direction(direction), self, door)
