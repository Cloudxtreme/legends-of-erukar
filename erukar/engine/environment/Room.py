from erukar.engine.model.Containable import Containable
from erukar.engine.model.Direction import Direction
from erukar.engine.environment import Door, Wall, Passage

class Room(Containable):
    def __init__(self, coordinates=(0,0)):
        super().__init__([],"","")
        self.floor = None
        self.ceiling = None
        self.coordinates = coordinates
        self.connections = {direction: Passage() for direction in Direction}

    def connect_room(self, direction, other_room, door=None):
        if other_room is not self:
            self.connections[direction] = Passage(room=other_room, door=door)

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
        return self.description

    def add_door(self, direction, door):
        self.connections[direction].door = door
        other_dir = self.invert_direction(direction)
        self.connections[direction].room.connections[other_dir].door = door

    def describe_in_direction(self, direction, draw_walls=False):
        con = self.connections[direction]

        if con is not None:
            if con.door is not None:
                if type(con.door) is Wall and draw_walls:
                    return con.door.on_inspect(direction.name)
                if type(con.door) is Door:
                    return self.describe_door_in_direction(con.door, con.room, direction.name)

            if con.room is not None:
                return con.room.inspect_peek(direction.name)

        return None

    def describe_door_in_direction(self, door, room, direction):
        door_result = door.on_inspect(direction)
        if door.status == Door.Open:
            door_result += ' ' + room.inspect_peek(direction)
        return door_result

    def describe(self):
        dirs = ['{0}:\t{1}'.format(d.name, self.describe_in_direction(d, draw_walls=True)) for d in self.connections if self.connections[d].is_not_empty()]
        contents = [c.describe() for c in self.contents if c.describe() is not None]
        return ' '.join([self.description] + contents + ['\n'] + ['\n' + d for d in dirs])
