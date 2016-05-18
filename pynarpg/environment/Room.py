from pynarpg.model.EnvironmentPiece import EnvironmentPiece

class Room(EnvironmentPiece):
    North = 0
    East = 1
    South = 2
    West = 3

    def __init__(self):
        self.contents = []
        self.connections = [None for x in range(0, 4)]
        self.nesw_descriptions = ['TBD' for x in range(0,4)]
        self.description = ''

    def connect_room(self, direction, other_room, door=None):
        self.connections[direction] = { "room": other_room, "door": door}

    def add(self, item):
        self.contents.append(item)

    def invert_direction(self, direction):
        return (direction + 2) % 4

    def get_in_direction(self, direction):
        return self.connections[direction]

    def coestablish_connection(self, direction, other_room, door=None):
        '''Establishes a connection to both rooms'''
        self.connect_room(direction, other_room, door)
        other_room.connect_room(self.invert_direction(direction), self, door)
