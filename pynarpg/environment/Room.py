from pynarpg.model.RpgEntity import RpgEntity
from pynarpg.model.Direction import Direction
from pynarpg.environment.EntityLocation import EntityLocation

class Room(RpgEntity):

    def __init__(self):
        self.contents = []
        self.connections = {direction: None for direction in Direction}
        self.nesw_descriptions = {direction: 'TBD' for direction in Direction}
        self.description = ''

    def connect_room(self, direction, other_room, door=None):
        self.connections[direction] = { "room": other_room, "door": door}

    def add(self, item, adjective, preposition, plural=False):
        self.contents.append(EntityLocation(item, adjective, preposition, plural))

    def invert_direction(self, direction):
        return Direction( (direction.value + 2) % 4 )

    def get_in_direction(self, direction):
        return self.connections[direction]

    def coestablish_connection(self, direction, other_room, door=None):
        '''Establishes a connection to both rooms'''
        self.connect_room(direction, other_room, door)
        other_room.connect_room(self.invert_direction(direction), self, door)

    def describe(self):
        return ' '.join([self.description] + [c.describe() for c in self.contents if c.describe() is not None])

    def remove(self, entity):
        target = next((x for x in self.contents if x is entity or (hasattr(x, 'entity') and x.entity is entity)), None)
        self.contents.remove(entity)
