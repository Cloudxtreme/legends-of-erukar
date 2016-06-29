from erukar.engine.model.Containable import Containable
from erukar.engine.model.Direction import Direction
from erukar.engine.environment.Passage import Passage
from erukar.engine.environment.Surface import Surface

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

    def describe_in_direction(self, direction, inspect_walls=False):
        con = self.connections[direction]
        return con.on_inspect(direction, inspect_walls)

    def describe(self):
        room_descriptions = list(self.generate_room_descriptions())
        directions = list(self.generate_direction_descriptions())
        contents = list(self.generate_content_descriptions())
        return ' '.join(room_descriptions + contents + ['\n'] + directions)

    def generate_room_descriptions(self):
        yield self.description
        if self.floor is not None:
            yield self.floor.on_inspect()
        if self.ceiling is not None:
            yield self.ceiling.on_inspect()

    def generate_direction_descriptions(self):
        '''Generator for creating a list of directional descriptions'''
        for direction in self.connections:
            res = self.describe_in_direction(direction, inspect_walls=False)
            if res is not None:
                yield '\n{0}:\t{1}'.format(direction.name, res)

    def generate_content_descriptions(self):
        '''Generator for creating a list of content descriptions'''
        for content in self.contents:
            description = content.describe()
            if description is not None:
                yield description

    def walls(self):
        '''Generator for getting only the walls in this room'''
        for direction in self.connections:
            passage = self.connections[direction]
            if passage.room is None and isinstance(passage.door, Surface):
                yield passage.door
