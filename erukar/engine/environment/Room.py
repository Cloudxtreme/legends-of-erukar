from erukar.engine.model.Containable import Containable
from erukar.engine.model.Direction import Direction
from erukar.engine.model.EntityLocation import EntityLocation

class Room(Containable):
    def __init__(self):
        super().__init__()
        self.connections = {direction: None for direction in Direction}
        self.nesw_descriptions = {direction: 'TBD' for direction in Direction}

    def connect_room(self, direction, other_room, door=None):
        self.connections[direction] = { "room": other_room, "door": door}

    def invert_direction(self, direction):
        return Direction( (direction.value + 2) % 4 )

    def get_in_direction(self, direction):
        return self.connections[direction]

    def coestablish_connection(self, direction, other_room, door=None):
        '''Establishes a connection to both rooms'''
        self.connect_room(direction, other_room, door)
        other_room.connect_room(self.invert_direction(direction), self, door)

    def on_inspect(self, direction):
        return 'To your {0} you see a room. {1}'.format(direction, self.describe())
