from erukar.engine.factories.FactoryBase import FactoryBase
from erukar.engine.environment import *
from erukar.engine.model import Direction
from erukar.engine.model.CoordinateTranslator import CoordinateTranslator
import numpy as np
import math, random

class DungeonGenerator(FactoryBase):
    def __init__(self):
        '''
        The following probabilities determine the likelihood of the number of
        branches, e.g. here we have a 70% chance of 1 new connection, 20% chance
        of 2 new connections, and a 10% chance of a 4-way room
        '''
        self.branching_probabilities = [0.0, 0.50, 0.90]
        # The Hallway Bias is the bias of the dungeon to continue forward instead of cornering
        self.hallway_bias = 0.3
        self.avg_rooms = 15

    def generate(self):
        self.dungeon = Dungeon()
        num_rooms = math.floor(np.random.gamma(self.avg_rooms, 1.0)) + Dungeon.minimum_rooms
        self.create_rooms(num_rooms)

        return self.dungeon

    def create_rooms(self, num_rooms):
        '''Create X number of rooms'''
        self.dungeon.rooms = [Room() for x in range(num_rooms)]
        self.dungeon.dungeon_map[(0,0)] = self.dungeon.rooms[0]
        self.connect_rooms()
        self.generate_descriptions()
        self.fill_walls()

    def connect_rooms(self):
        '''Connect a list of rooms to each other'''
        for index, room in enumerate(self.dungeon.rooms):
            for connection_num in range(self.number_of_connections()):
                self.connect_randomly(room)

    def unconnected(self):
        '''Shortcut to a generator that provides unconnected rooms'''
        return (r for r in self.dungeon.rooms[1:] if len(self.possible_directions(r)) == 4)

    def generate_descriptions(self):
        ''' Add descriptions '''
        for i,r in enumerate(self.dungeon.rooms):
            r.description = 'This is the {0}th room at ({1}, {2}).'.format(i, *r.coordinates)

    def fill_walls(self):
        '''Fill in the abyss with walls (ugly, need to optimize)'''
        for room in self.dungeon.rooms:
            for direction in self.possible_directions(room):
                room.connections[direction] = { 'door': Wall(), 'room': None }

    def connect_randomly(self, origin):
        '''Connect a room (origin) to a destination room in some random direction'''
        if not any(self.possible_directions(origin)): return

        direction = self.random_direction(origin)
        new_coords = CoordinateTranslator.translate(origin.coordinates, direction)
        if new_coords in self.dungeon.dungeon_map:
            destination = self.dungeon.dungeon_map[new_coords]
        else:
            uncon = next(self.unconnected(), None)
            if uncon is None: return
            destination = uncon

        origin.coestablish_connection(direction, destination)
        self.link_coordinates_to_room(new_coords, destination)

    def link_coordinates_to_room(self, coordinates, destination):
        '''
        Links the room's coordinates and the dungeon map's coordinates, removing any
        duplications
        '''
        destination.coordinates = coordinates
        pre_existing = [r for r in self.dungeon.dungeon_map if self.dungeon.dungeon_map[r] is destination]
        for room in pre_existing:
            self.dungeon.dungeon_map.pop(room, None)
        self.dungeon.dungeon_map[(destination.coordinates)] = destination

    def possible_directions(self, room):
        '''Get all directions for a room that are not already specified'''
        return [d for d in room.connections \
            if room.connections[d]['door'] is None and room.connections[d]['room'] is None]

    def random_direction(self, room):
        '''Find a random direction implementing biases'''
        # Build out the random_set using biases and an existing room connection
        basis_direction = next((x for x in room.connections if room.connections[x] is not None), Direction.North)
        dirs = (np.arange(3) + basis_direction.value + 1) % 4
        side_bias = (1.0-self.hallway_bias) / 2
        random_set = [0, side_bias, side_bias + self.hallway_bias]

        # evaluate a random number vs. the random_set
        rand = random.random()
        random_direction = [dirs[i] for i, _ in enumerate(dirs) if rand > random_set[i]][-1]
        return Direction(random_direction)

    def number_of_connections(self):
        '''
        Get a random number of connections, where 70% of the time there will be
        a single connection, 20% of the time there will be two, and 10% of the
        time there will be three. Probabilities are determined by the constant
        branching_probabilities
        '''
        rand = random.random()
        return sum(1 for pct in self.branching_probabilities if rand > pct)
