from erukar.engine.factories.FactoryBase import FactoryBase
from erukar.engine.environment import *
from erukar.engine.model import Direction
import numpy as np
import math, random

class DungeonGenerator(FactoryBase):
    minimum_rooms = 3

    def __init__(self):
        self.hallway_bias = 0.6
        self.branching_probabilities = [0.0, 0.70, 0.90]
        # the following will belong on a Dungeon object that will be passed around
        self.dungeon_map = {}
        self.rooms = []

    def generate(self):
        num_rooms = math.floor(np.random.gamma(15, 1.0)) + DungeonGenerator.minimum_rooms
        print('There are {0} rooms in this dungeon'.format(num_rooms))
        return self.create_rooms(num_rooms)

    def create_rooms(self, num_rooms):
        '''Create X number of rooms'''
        self.rooms = [Room() for x in range(num_rooms)]
        self.dungeon_map[(0,0)] = self.rooms[0]
        self.connect_rooms()
        self.generate_descriptions()
        self.fill_walls()
        return self.rooms

    def map_to_string(self):
        '''Converts the dungeon_map into a readable map for the user'''
        max_x, max_y = [max([m[i] for m in self.dungeon_map]) for i in range(2)]
        min_x, min_y = [min([m[i] for m in self.dungeon_map]) for i in range(2)]

        dnjn_map = [['#' if (x,y) in self.dungeon_map else ' ' for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]
##
        # ALWAYS have the origin at 0,0
        dnjn_map[-min_y][-min_x] = 'o'

        return '\n'.join(''.join(map(str, y)) for y in reversed(dnjn_map))

    def connect_rooms(self):
        '''Connect a list of rooms to each other'''
        for origin, index in zip(self.rooms, range(len(self.rooms))):
            num_connections = self.number_of_connections()
            for connection_num in range(num_connections):
                self.connect_randomly(origin)

    def unconnected(self):
        return [r for r in self.rooms[1:] if len(self.possible_directions(r)) == 4]

    def generate_descriptions(self):
        ''' Add descriptions '''
        for r,i in zip(self.rooms, range(len(self.rooms))):
            r.description = 'This is the {0}th room at ({1}, {2}).'.format(i, *r.coordinates)

    def fill_walls(self):
        '''Fill in the abyss with walls (ugly, need to optimize)'''
        for room in self.rooms:
            for direction in self.possible_directions(room):
                room.connections[direction] = { 'door': Wall() }

    def connect_randomly(self, origin):
        '''Connect a room (origin) to a destination room in some random direction'''
        if not any(self.possible_directions(origin)): return

        direction = self.random_direction(origin)
        new_coords = self.to_coordinate(origin.coordinates, direction)
        if new_coords in self.dungeon_map:
            destination = self.dungeon_map[new_coords]
        else:
            uncon = self.unconnected()
            if len(uncon) == 0: return
            destination = uncon[0]

        origin.coestablish_connection(direction, destination)
        self.link_coordinates_to_room(new_coords, destination)

    def link_coordinates_to_room(self, coordinates, destination):
        '''
        Links the room's coordinates and the dungeon map's coordinates, removing any
        duplications
        '''
        destination.coordinates = coordinates
        pre_existing = [r for r in self.dungeon_map if self.dungeon_map[r] is destination]
        for room in pre_existing:
            self.dungeon_map.pop(room, None)
        self.dungeon_map[(destination.coordinates)] = destination

    def possible_directions(self, room):
        '''Get all directions for a room that are not already specified'''
        return [d for d in room.connections if room.connections[d] is None]

    def random_direction(self, room):
        '''Find a random direction implementing biases'''
        # Build out the random_set using biases and an existing room connection
        basis_direction = next((x for x in room.connections if room.connections[x] is not None), Direction.North)
        dirs = (np.arange(3) + basis_direction.value + 1) % 4
        side_bias = (1.0-self.hallway_bias) / 2
        random_set = [0, side_bias, side_bias + self.hallway_bias]

        # evaluate a random number vs. the random_set
        rand = random.random()
        directional_matches = [dirs[i] for i in range(len(dirs)) if rand > random_set[i]]
        return Direction(directional_matches[-1])

    def number_of_connections(self):
        '''
        Get a random number of connections, where 70% of the time there will be
        a single connection, 20% of the time there will be two, and 10% of the
        time there will be three. Probabilities are determined by the constant
        branching_probabilities
        '''
        rand = random.random()
        return sum([1 for pct in self.branching_probabilities if rand > pct])

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
