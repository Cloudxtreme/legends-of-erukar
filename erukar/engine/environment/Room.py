from erukar.engine.model.Containable import Containable
from erukar.engine.model.Direction import Direction
from erukar.engine.model.EntityLocation import EntityLocation
from erukar.engine.environment import Door, Wall

class Room(Containable):
    def __init__(self, coordinates=(0,0)):
        super().__init__()
        self.coordinates = coordinates
        self.connections = {direction: { "room": None, "door": None} for direction in Direction}

    def connect_room(self, direction, other_room, door=None):
        if other_room is not self:
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
        return self.description

    def inspect_peek(self, direction):
        return 'To your {0} you see a room.'.format(direction)

    def describe_in_direction(self, direction, draw_walls=False):
        con = self.connections[direction]

        if con is not None:
            if con['door'] is not None:
                if type(con['door']) is Wall and draw_walls:
                    return con['door'].on_inspect(direction.name)
                if type(con['door']) is Door and con['door'].status != Door.Open:
                    return con['door'].on_inspect(direction.name)

            if 'room' in con and con['room'] is not None:
                return con['room'].inspect_peek(direction.name)

        return None

    def describe(self):
        dirs = [self.describe_in_direction(d, draw_walls=True) for d in self.connections]
        contents = [c.describe() for c in self.contents if c.describe() is not None]
        return ' '.join([self.description] + contents + ['\n'] + ['\n'+d for d in dirs if d is not None])
