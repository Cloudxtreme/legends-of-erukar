from erukar.engine.factories.FactoryBase import FactoryBase
from erukar.engine.environment import *
from erukar.engine.model import Direction
import numpy as np
import math, random

class DungeonGenerator(FactoryBase):
    minimum_rooms = 3
    def __init__(self):
        # the following will belong on a Dungeon object that will be passed around
        self.dungeon_map = {}
        self.rooms = []

    def generate(self):
        num_rooms = math.floor(np.random.gamma(7.5, 1.0)) + DungeonGenerator.minimum_rooms
        return self.create_rooms(num_rooms)

    def create_rooms(self, num_rooms):
        '''Create X number of rooms'''
        self.rooms = [Room() for x in range(num_rooms)]
        self.connect_rooms()
        self.generate_descriptions()
        self.fill_walls()
        return self.rooms

    def map_to_string(self):
        '''Converts the dungeon_map into a readable map for the user'''
        max_x, max_y = [max([m[i] for m in self.dungeon_map]) for i in range(2)]
        min_x, min_y = [min([m[i] for m in self.dungeon_map]) for i in range(2)]

        # This really should be cleaned up
        result_str = ''
        for y in range(min_y-1, max_y+1):
            # new_row is used to prevent dealing with immutability in strings
            new_row = [' ' for i in range(min_x-1, max_x+1)]
            for x in [xi for xi in range(min_x-1, max_x+1) if (xi,y) in self.dungeon_map]:
                # The actual indices may be negative, so account for that
                pt_index = x - min_x
                # default to a hash as it is the most probable option
                new_row[pt_index] = '#'
                # For origin
                if (x,y) == (0,0):
                    new_row[pt_index] = 'o'
            result_str = ''.join(new_row) + '\n' + result_str
        return result_str

    def connect_rooms(self):
        '''Connect a list of rooms to each other'''
        self.dungeon_map[(0,0)] = self.rooms[0]

        for origin_room, index in zip(self.rooms, range(len(self.rooms))):
            self.generate_connections(origin_room, index)

    def connected(self):
        return [r for r in self.rooms if len(self.possible_directions(r)) < 4]

    def unconnected(self):
        return [r for r in self.rooms if len(self.possible_directions(r)) == 4]

    def generate_descriptions(self):
        ''' Add descriptions '''
        for r,i in zip(self.rooms, range(len(self.rooms))):
            r.description = 'This is the {0}th room at ({1}, {2}).'.format(i, *r.coordinates)

    def fill_walls(self):
        '''Fill in the abyss with walls (ugly, need to optimize)'''
        for room in self.rooms:
            for direction in self.possible_directions(room):
                room.connections[direction] = { 'door': Wall() }

    def generate_connections(self, origin, index):
        num_connections = max(0, len(self.rooms) - index - self.number_of_connections())
        for connection_num in range(num_connections):
            self.connect_randomly(origin)

    def connect_randomly(self, origin):
        '''Connect a room (origin) to a destination room in some random direction'''
        directions = self.possible_directions(origin)
        if not any(directions): return

        # Use the origin room and look in each direction
        # if there's a room there, connect to it.
        # If not, grab a room with empty coordinates that isn't origin

        direction = random.choice(directions)
        new_coords = self.to_coordinate(origin.coordinates, direction)
        if new_coords in self.dungeon_map:
            destination = self.dungeon_map[new_coords]
        else:
            if len(self.unconnected()) == 0:
                return
            destination = self.unconnected()[0]

        origin.coestablish_connection(direction, destination)
        destination.coordinates = self.to_coordinate(origin.coordinates, direction)
        self.dungeon_map[(destination.coordinates)] = destination


    def possible_directions(self, room):
        '''Get all directions for a room that are not already specified'''
        return [d for d in room.connections if room.connections[d] is None]

    def number_of_connections(self):
        # y = 1 + heaviside(x-0.6) + heaviside(x-0.9) from x=[0, 1.0]
        rand = random.random()
        return 1 + sum([1 for pct in [0.66, 0.92] if rand > pct])

    def to_coordinate(self, origin_coord, direction):
        '''Hmm, how do I clean this up?'''
        if direction is Direction.North:
            return (origin_coord[0], origin_coord[1]+1)
        if direction is Direction.East:
            return (origin_coord[0]+1, origin_coord[1])
        if direction is Direction.South:
            return (origin_coord[0], origin_coord[1]-1)
        if direction is Direction.West:
            return (origin_coord[0]-1, origin_coord[1])
        # Otherwise, just return the origin point... used when first generating
        return (0, 0)
